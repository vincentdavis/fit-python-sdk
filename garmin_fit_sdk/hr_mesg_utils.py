'''hr_mesg_utils.py: Contains the functions for merging hr_mesgs to record_mesgs'''

###########################################################################################
# Copyright 2024 Garmin International, Inc.
# Licensed under the Flexible and Interoperable Data Transfer (FIT) Protocol License; you
# may not use this file except in compliance with the Flexible and Interoperable Data
# Transfer (FIT) Protocol License.
###########################################################################################
# ****WARNING****  This file is auto-generated!  Do NOT edit this file.
# Profile Version = 21.133.0Release
# Tag = production/release/21.133.0-0-g6002091
############################################################################################


from datetime import datetime

from . import util


def merge_heart_rates(hr_mesgs, record_mesgs):
    '''Takes the list of heart rate messages and merges them into the record messages.'''
    if hr_mesgs is None or record_mesgs is None or len(hr_mesgs) == 0 or len(record_mesgs) == 0:
        return

    heartrates = expand_heart_rates(hr_mesgs)

    heartrate_index = 0
    record_range_start_time = None

    for i in range(len(record_mesgs)):
        message = record_mesgs[i]

        hr_sum = 0
        hr_sum_count = 0

        record_range_end_time = seconds_since_fit_epoch(message['timestamp'])

        if record_range_start_time is None:
            record_range_start_time = record_range_end_time

        if record_range_start_time == record_range_end_time:
            record_range_start_time -= 1
            heartrate_index = heartrate_index - 1 if heartrate_index >= 1 else 0

        finding_in_range_hr_mesgs = True
        while(finding_in_range_hr_mesgs and (heartrate_index < len(heartrates))):
            heart_rate = heartrates[heartrate_index]

            # Check if the heartrate timestamp is > record start time
            # and if the heartrate timestamp is <= to record end time
            if heart_rate['timestamp'] > record_range_start_time and heart_rate['timestamp'] <= record_range_end_time:
                hr_sum += heart_rate['heart_rate']
                hr_sum_count += 1
            # Check if the heartrate timestamp exceeds the record time
            elif heart_rate['timestamp'] > record_range_end_time:
                finding_in_range_hr_mesgs = False

                if hr_sum_count > 0:
                    # Update record's heart rate value
                    #avg_hr = round(hr_sum / hr_sum_count, 0)
                    avg_hr = int((hr_sum / hr_sum_count) + .5)
                    message['heart_rate'] = avg_hr
                # Reset HR average accumulators
                hr_sum = 0
                hr_sum_count = 0
                record_range_start_time = record_range_end_time

                # Breaks out of finding_in_range_hr_messages while loop without incrementing heartrate_index
                break
            heartrate_index += 1


def expand_heart_rates(hr_mesgs):
    '''Takes the heart rate messages and expands them to 250ms increments.'''
    GAP_INCREMENT_MILLISECONDS = 250
    GAP_INCREMENT_SECONDS = GAP_INCREMENT_MILLISECONDS / 1000.0
    GAP_MAX_MILLISECONDS = 5000
    GAP_MAX_STEPS = GAP_MAX_MILLISECONDS / GAP_INCREMENT_MILLISECONDS

    if hr_mesgs is None or len(hr_mesgs) == 0:
        return []

    anchor_event_timestamp = 0.0
    anchor_timestamp = None

    heartrates = []

    for message in hr_mesgs:
        if message is None:
            __raise_error("HR message must not be None.")

        event_timestamps = message['event_timestamp'] if isinstance(message['event_timestamp'], list) else [message['event_timestamp']]
        filtered_bpm = message['filtered_bpm'] if isinstance(message['filtered_bpm'], list) else [message['filtered_bpm']]

        # Update HR anchor timestamp if present
        if 'timestamp' in message and message['timestamp'] is not None:
            anchor_timestamp = seconds_since_fit_epoch(message['timestamp'])

            if message['fractional_timestamp'] is not None:
                anchor_timestamp += message['fractional_timestamp']

            if len(event_timestamps) == 1:
                anchor_event_timestamp = event_timestamps[0]
            else:
                __raise_error("Anchor HR message must have at least one event_timestamp")

        if anchor_timestamp is None or anchor_event_timestamp is None:
            __raise_error("No anchor timestamp received in an HR message before delta HR messages")
        elif len(event_timestamps) != len(filtered_bpm):
            __raise_error("HR message with mismatching event timestamp and filtered bpm")

        for i in range(len(event_timestamps)):
            event_timestamp = event_timestamps[i]

            if event_timestamp < anchor_event_timestamp:
                if anchor_event_timestamp - event_timestamp > (0x400000):
                    event_timestamp += 0x400000
                else:
                    __raise_error("Anchor event_timestamp is greater than subsequent event_timestamp. This does not allow for correct delta caluclation.")


            current_hr = { 'timestamp': anchor_timestamp, 'heart_rate': filtered_bpm[i] }
            current_hr['timestamp'] += (event_timestamp - anchor_event_timestamp)

            # Carry the previous HR value forward across the gap to the current
            # HR value for up to 5 seconds in 250ms increments
            if len(heartrates) > 0:
                previous_hr = heartrates[len(heartrates) - 1]
                gap_in_milliseconds = abs(current_hr['timestamp'] - previous_hr['timestamp']) * 1000
                step = 1

                while(gap_in_milliseconds > GAP_INCREMENT_MILLISECONDS and step <= GAP_MAX_STEPS):
                    gap_hr = { 'timestamp': previous_hr['timestamp'], 'heart_rate': previous_hr['heart_rate'] }
                    gap_hr['timestamp'] += (GAP_INCREMENT_SECONDS * step)
                    heartrates.append(gap_hr)

                    gap_in_milliseconds -= GAP_INCREMENT_MILLISECONDS
                    step += 1

            heartrates.append(current_hr)
    return heartrates

def seconds_since_fit_epoch(timestamp):
    '''Gives the time in seconds since the fit epoch.'''
    if isinstance(timestamp, datetime):
        return (timestamp.timestamp() - util.FIT_EPOCH_S)

    return timestamp

def __raise_error(error = ""):
        message = f"FIT Runtime Error {error}"
        raise RuntimeError(message)
