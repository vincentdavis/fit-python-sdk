'''data.py: Contains various byte arrays which are reused in testing the FIT SDK.'''

###########################################################################################
# Copyright 2023 Garmin International, Inc.
# Licensed under the Flexible and Interoperable Data Transfer (FIT) Protocol License; you
# may not use this file except in compliance with the Flexible and Interoperable Data
# Transfer (FIT) Protocol License.
###########################################################################################


class Data:
    '''Helper class that holds example fit files and byte arrays to be used for testing.'''

    fit_file_invalid = bytearray([
        0x0E, 0x20, 0x9F, 0x03, 0x64, 0x00, 0x00, 0x00,
        0x2E, 0x99, 0x49, 0x54, 0xB9, 0xE3, 0x00, 0x00
    ])

    fit_file_minimum = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x00, 0x00, 0x00, 0x00,
        0x2E, 0x46, 0x49, 0x54, 0x8D, 0x48, 0x00, 0x00,
    ])

    fit_file_incorrect_data_size = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0xFF, 0x00, 0x00, 0x00,
        0x2E, 0x46, 0x49, 0x54, 0x8D, 0x48, 0x00, 0x00,
    ])

    fit_file_short = bytearray([
        0x0E, 0x20, 0x9F, 0x03, 0x64, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0xB9, 0xE3, 0x40, 0x00, 0x00, 0x00, 0x00, 0x08, 0x03, 0x04, 0x8C, 0x04,
        0x04, 0x86, 0x08, 0x14, 0x07, 0x01, 0x02, 0x84, 0x02, 0x02, 0x84, 0x05,
        0x02, 0x84, 0x06, 0x02, 0x84, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0xCA, 0x9A, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x02, 0x40, 0x00,
        0x00, 0xD3, 0x00, 0x05, 0xFD, 0x04, 0x86, 0x03, 0x02, 0x84, 0x04, 0x02,
        0x84, 0x00, 0x01, 0x02, 0x01, 0x01, 0x02, 0x00, 0x00, 0xCA, 0x9A, 0x3B,
        0x32, 0x00, 0x37, 0x00, 0x2C, 0x2E, 0x87, 0x4F
    ])

    fit_file_short_new = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x24, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54, 0x8E, 0xA3,  # File Header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01, 0x02, 0x84, 0x04, 0x04, 0x86, 0x08, 0x0A, 0x07, # Message Definition
        0x00, 0x04, 0x01, 0x00, 0x00, 0xCA, 0x9A, 0x3B, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x00, # Message
        0x5D, 0xF2  # CRC
    ])

    fit_file_short_compressed_timestamp = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x24, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54, 0x8E, 0xA3, # File Header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01, 0x02, 0x84, 0x04, 0x04, 0x86, 0x08, 0x0A, 0x07, # Message Definition
        0x80, 0x04, 0x01, 0x00, 0x00, 0xCA, 0x9A, 0x3B, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x00, # Message
        0x5D, 0xF2
    ])

    fit_file_short_new_invalid_crc = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x24, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54, 0x8E, 0xA3,  # File Header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01, 0x02, 0x84, 0x04, 0x04, 0x86, 0x08, 0x0A, 0x07, # Message Definition
        0x00, 0x04, 0x01, 0x00, 0x00, 0xCA, 0x9A, 0x3B, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x00, # Message
        0xFF, 0xFF  # CRC
    ])

    fit_file_short_none_array = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x24, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54, 0x8E, 0xA3,  # File Header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01, 0x02, 0x84, 0x04, 0x04, 0x86, 0x08, 0x0A, 0x07, # Message Definition
        0x00, 0x04, 0x01, 0x00, 0x00, 0xCA, 0x9A, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # Message
        0x6C, 0x15  # CRC
    ])

    fit_file_short_with_wrong_field_def_size = bytearray([
        0x0E, 0x20, 0x8B, 0x08, 0x21, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54, 0x8E, 0xA3, # File Header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x01, 0x02, 0x84, 0x04, 0x01, 0x86, 0x08, 0x0A, 0x07, # Message Definition
        0x00, 0x04, 0x01, 0x00, 0x12, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x00, # Message
        0x65, 0xFE # CRC
        ])

    fit_file_arrays = bytearray([
        0x0E, 0x20, 0x9F, 0x03, 0x32, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0x3C, 0xF5, 0x40, 0x00, 0x01, 0x00, 0x00, 0x03, 0x01, 0x02, 0x84, 0x00,
        0x01, 0x00, 0x03, 0x04, 0x8C, 0x00, 0x00, 0xFF, 0x04, 0x00, 0x00, 0x30,
        0x39, 0x40, 0x00, 0x01, 0x00, 0x0C, 0x03, 0x03, 0x05, 0x07, 0x0A, 0x04,
        0x02, 0x13, 0x02, 0x00, 0x00, 0x54, 0x65, 0x73, 0x74, 0x00, 0xFF, 0xFF,
        0xFF, 0xFF, 0x05, 0x01, 0x5C, 0x21
    ])

    fit_file_chained = bytearray([
        0x0E, 0x20, 0x9F, 0x03, 0x64, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0xB9, 0xE3, 0x40, 0x00, 0x00, 0x00, 0x00, 0x08, 0x03, 0x04, 0x8C, 0x04,
        0x04, 0x86, 0x08, 0x14, 0x07, 0x01, 0x02, 0x84, 0x02, 0x02, 0x84, 0x05,
        0x02, 0x84, 0x06, 0x02, 0x84, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x02, 0x40, 0x00,
        0x00, 0xD3, 0x00, 0x05, 0xFD, 0x04, 0x86, 0x03, 0x02, 0x84, 0x04, 0x02,
        0x84, 0x00, 0x01, 0x02, 0x01, 0x01, 0x02, 0x00, 0x00, 0xCA, 0x9A, 0x3B,
        0x32, 0x00, 0x37, 0x00, 0x2C, 0x2E, 0x7C, 0xD5,
        0x0E, 0x20, 0x9F, 0x03, 0x64, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0xB9, 0xE3, 0x40, 0x00, 0x00, 0x00, 0x00, 0x08, 0x03, 0x04, 0x8C, 0x04,
        0x04, 0x86, 0x08, 0x14, 0x07, 0x01, 0x02, 0x84, 0x02, 0x02, 0x84, 0x05,
        0x02, 0x84, 0x06, 0x02, 0x84, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x02, 0x40, 0x00,
        0x00, 0xD3, 0x00, 0x05, 0xFD, 0x04, 0x86, 0x03, 0x02, 0x84, 0x04, 0x02,
        0x84, 0x00, 0x01, 0x02, 0x01, 0x01, 0x02, 0x00, 0x00, 0xCA, 0x9A, 0x3B,
        0x32, 0x00, 0x37, 0x00, 0x2C, 0x2E, 0x7C, 0xD5
    ])

    fit_file_800m_repeats_little_endian = bytearray([
        0x0E, 0x10, 0x8D, 0x08, 0xDB, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0xDE, 0xB8, 0x40, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x01, 0x00, 0x01,
        0x02, 0x84, 0x02, 0x02, 0x84, 0x04, 0x04, 0x86, 0x03, 0x04, 0x8C, 0x00,
        0x05, 0xFF, 0x00, 0x00, 0x00, 0x12, 0xAD, 0x66, 0x3D, 0x38, 0xB6, 0xC1,
        0x0A, 0x40, 0x00, 0x00, 0x1A, 0x00, 0x04, 0x08, 0x15, 0x07, 0x04, 0x01,
        0x00, 0x0B, 0x01, 0x00, 0x06, 0x02, 0x84, 0x00, 0x52, 0x75, 0x6E, 0x6E,
        0x69, 0x6E, 0x67, 0x20, 0x38, 0x30, 0x30, 0x6D, 0x20, 0x52, 0x65, 0x70,
        0x65, 0x61, 0x74, 0x73, 0x00, 0x01, 0xFF, 0x05, 0x00, 0x40, 0x00, 0x00,
        0x1B, 0x00, 0x08, 0x02, 0x04, 0x86, 0xFE, 0x02, 0x84, 0x07, 0x01, 0x00,
        0x01, 0x01, 0x00, 0x03, 0x01, 0x00, 0x04, 0x04, 0x86, 0x05, 0x04, 0x86,
        0x06, 0x04, 0x86, 0x00, 0x80, 0x1A, 0x06, 0x00, 0x00, 0x00, 0x02, 0x01,
        0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x80, 0x38, 0x01, 0x00, 0x01, 0x00, 0x00, 0x01, 0x01, 0x04,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x20, 0x4E, 0x00, 0x00, 0x02, 0x00, 0x01, 0x01, 0x01, 0x02, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00,
        0x00, 0x00, 0x03, 0x00, 0xFF, 0x06, 0x02, 0x05, 0x00, 0x00, 0x00, 0xFF,
        0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0xA0, 0x86, 0x01, 0x00,
        0x04, 0x00, 0x03, 0x01, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0xAE, 0xC4
    ])

    fit_file_800m_repeats_big_endian = bytearray([
        0x0E, 0x20, 0x9F, 0x03, 0xDB, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0xF2, 0xD7, 0x40, 0x00, 0x01, 0x00, 0x00, 0x05, 0x00, 0x01, 0x00, 0x01,
        0x02, 0x84, 0x02, 0x02, 0x84, 0x04, 0x04, 0x86, 0x03, 0x04, 0x8C, 0x00,
        0x05, 0x00, 0xFF, 0x00, 0x00, 0x3D, 0x66, 0xAD, 0x12, 0x0A, 0xC1, 0xB6,
        0x38, 0x40, 0x00, 0x01, 0x00, 0x1A, 0x04, 0x08, 0x15, 0x07, 0x04, 0x01,
        0x00, 0x0B, 0x01, 0x00, 0x06, 0x02, 0x84, 0x00, 0x52, 0x75, 0x6E, 0x6E,
        0x69, 0x6E, 0x67, 0x20, 0x38, 0x30, 0x30, 0x6D, 0x20, 0x52, 0x65, 0x70,
        0x65, 0x61, 0x74, 0x73, 0x00, 0x01, 0xFF, 0x00, 0x05, 0x40, 0x00, 0x01,
        0x00, 0x1B, 0x08, 0x02, 0x04, 0x86, 0xFE, 0x02, 0x84, 0x07, 0x01, 0x00,
        0x01, 0x01, 0x00, 0x03, 0x01, 0x00, 0x04, 0x04, 0x86, 0x05, 0x04, 0x86,
        0x06, 0x04, 0x86, 0x00, 0x00, 0x06, 0x1A, 0x80, 0x00, 0x00, 0x02, 0x01,
        0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x01, 0x38, 0x80, 0x00, 0x01, 0x00, 0x01, 0x01, 0x00,
        0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x4E, 0x20, 0x00, 0x02, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00,
        0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x01, 0x00, 0x03, 0xFF, 0x06, 0x02, 0x00, 0x00, 0x00, 0x05, 0xFF,
        0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x01, 0x86, 0xA0,
        0x00, 0x04, 0x03, 0x01, 0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x87, 0x67
    ])

    fit_file_dev_data_missing_field_description = bytearray([
        0x0E, 0x20, 0x64, 0x00, 0xD1, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0x12, 0x7E, 0x40, 0x00, 0x01, 0x00, 0x00, 0x05, 0x00, 0x01, 0x00, 0x01,
        0x02, 0x84, 0x02, 0x02, 0x84, 0x04, 0x04, 0x86, 0x03, 0x04, 0x8C, 0x00,
        0x04, 0x00, 0xFF, 0x00, 0x00, 0x3D, 0x5D, 0x38, 0xBD, 0x1E, 0x29, 0x25,
        0x9B, 0x60, 0x00, 0x01, 0x00, 0x14, 0x09, 0xFD, 0x04, 0x86, 0x05, 0x04,
        0x86, 0x06, 0x02, 0x84, 0x03, 0x01, 0x02, 0x04, 0x01, 0x02, 0x07, 0x02,
        0x84, 0x02, 0x02, 0x84, 0x00, 0x04, 0x85, 0x01, 0x04, 0x85, 0x01, 0x01,
        0x01, 0x00, 0x00, 0x3D, 0x5D, 0x38, 0xBD, 0x00, 0x00, 0x00, 0x00, 0x03,
        0xE8, 0x7E, 0x00, 0x00, 0x96, 0x07, 0x49, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x7E, 0x00, 0x3D, 0x5D, 0x38, 0xBE, 0x00, 0x00, 0x00,
        0x64, 0x03, 0xE8, 0x86, 0x01, 0x00, 0x96, 0x07, 0x4E, 0x7F, 0xFF, 0xFF,
        0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0x86, 0x00, 0x3D, 0x5D, 0x38, 0xBF, 0x00,
        0x00, 0x00, 0xC8, 0x03, 0xE8, 0x8E, 0x02, 0x00, 0x96, 0x07, 0x53, 0x7F,
        0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0x8E, 0x00, 0x3D, 0x5D, 0x38,
        0xC0, 0x00, 0x00, 0x01, 0x2C, 0x03, 0xE8, 0x96, 0x03, 0x00, 0x96, 0x07,
        0x58, 0x7F, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0x96, 0x40, 0x00,
        0x01, 0x00, 0x22, 0x04, 0xFD, 0x04, 0x86, 0x01, 0x02, 0x84, 0x05, 0x04,
        0x86, 0x00, 0x04, 0x86, 0x00, 0x3D, 0x5D, 0x46, 0xCD, 0x00, 0x01, 0x3D,
        0x5C, 0xF2, 0x6D, 0x00, 0x36, 0xEE, 0x80, 0x78, 0x3B
    ])

    fit_file_monitoring = bytearray([
        0x0E, 0x10, 0x28, 0x23, 0x37, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0x2C, 0xC6, 0x41, 0x00, 0x01, 0x00, 0x37, 0x03, 0xFD, 0x04, 0x86, 0x18,
        0x01, 0x0D, 0x03, 0x04, 0x86, 0x01, 0x3F, 0x2A, 0xE2, 0xFF, 0x61, 0x00,
        0x00, 0x00, 0x14, 0x01, 0x3F, 0x2A, 0xE2, 0xFF, 0x06, 0x00, 0x00, 0x00,
        0x3C, 0x01, 0x3F, 0x2A, 0xE2, 0xFF, 0x1E, 0x00, 0x00, 0x00, 0x1E, 0x01,
        0x3F, 0x2A, 0xE2, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x1E, 0xED, 0xF9
    ])

    fit_file_messages_with_no_fields = bytearray([
        0x0E, 0x20, 0x84, 0x52, 0x44, 0x00, 0x00, 0x00, 0x2E, 0x46, 0x49, 0x54,
        0x3A, 0x18, 0x40, 0x00, 0x01, 0x00, 0x69, 0x00, 0x41, 0x00, 0x01, 0x00,
        0x00, 0x07, 0x03, 0x04, 0x8C, 0x04, 0x04, 0x86, 0x01, 0x02, 0x84, 0x02,
        0x02, 0x84, 0x05, 0x02, 0x84, 0x00, 0x01, 0x00, 0xFB, 0x01, 0x0D, 0x01,
        0xCD, 0xC3, 0x1F, 0xAE, 0x3F, 0x92, 0x50, 0x78, 0x00, 0x01, 0x10, 0x22,
        0x00, 0x00, 0x20, 0xFF, 0x00, 0x01, 0xCD, 0xC3, 0x1F, 0xAE, 0x3F, 0x92,
        0x50, 0x78, 0x00, 0x01, 0x10, 0x22, 0x00, 0x00, 0x20, 0xFF, 0x25, 0xFB
    ])

    gear_change_data = [
    {
        "timestamp": 1024873717,
        "rear_gear_num": 5,
        "rear_gear": 24,
        "front_gear_num": 255,
        "front_gear": 22,
        "data": 385816581,
        "gear_change_data": 385816581
    },
    {
        "timestamp": 1024873760,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024873819,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024873850,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024874601,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024874624,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024874694,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024874698,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024874727,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024874755,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024874824,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024874829,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024874864,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024874913,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024874927,
        "rear_gear_num": 4,
        "rear_gear": 27,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16718596,
        "gear_change_data": 16718596
    },
    {
        "timestamp": 1024875097,
        "rear_gear_num": 5,
        "rear_gear": 24,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717829,
        "gear_change_data": 16717829
    },
    {
        "timestamp": 1024875097,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024875111,
        "rear_gear_num": 5,
        "rear_gear": 24,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717829,
        "gear_change_data": 16717829
    },
    {
        "timestamp": 1024875126,
        "rear_gear_num": 4,
        "rear_gear": 27,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16718596,
        "gear_change_data": 16718596
    },
    {
        "timestamp": 1024875251,
        "rear_gear_num": 3,
        "rear_gear": 31,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16719619,
        "gear_change_data": 16719619
    },
    {
        "timestamp": 1024875265,
        "rear_gear_num": 4,
        "rear_gear": 27,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16718596,
        "gear_change_data": 16718596
    },
    {
        "timestamp": 1024875271,
        "rear_gear_num": 5,
        "rear_gear": 24,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717829,
        "gear_change_data": 16717829
    },
    {
        "timestamp": 1024875291,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024875364,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024875388,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024875423,
        "rear_gear_num": 9,
        "rear_gear": 15,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16715529,
        "gear_change_data": 16715529
    },
    {
        "timestamp": 1024875515,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024875589,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024875615,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024875616,
        "rear_gear_num": 9,
        "rear_gear": 15,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16715529,
        "gear_change_data": 16715529
    },
    {
        "timestamp": 1024875621,
        "rear_gear_num": 10,
        "rear_gear": 13,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16715018,
        "gear_change_data": 16715018
    },
    {
        "timestamp": 1024875622,
        "rear_gear_num": 11,
        "rear_gear": 11,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16714507,
        "gear_change_data": 16714507
    },
    {
        "timestamp": 1024875651,
        "rear_gear_num": 9,
        "rear_gear": 15,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16715529,
        "gear_change_data": 16715529
    },
    {
        "timestamp": 1024875658,
        "rear_gear_num": 8,
        "rear_gear": 17,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716040,
        "gear_change_data": 16716040
    },
    {
        "timestamp": 1024875658,
        "rear_gear_num": 7,
        "rear_gear": 19,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16716551,
        "gear_change_data": 16716551
    },
    {
        "timestamp": 1024875665,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": None,
        "data": 16717062,
        "gear_change_data": 16717062
    },
    {
        "timestamp": 1024875695,
        "rear_gear_num": 6,
        "rear_gear": 21,
        "front_gear_num": 255,
        "front_gear": 22,
        "data": 385815814,
        "gear_change_data": 385815814
    }
]

    hrm_plugin_test_activity_expected = [
    1242209,
    1242212.0, 1242213.7314453125, 1242215.5029296875, 1242215.865234375, 1242216.9541015625, 1242218.3369140625, 1242219.6220703125, 1242219.9853515625,
    1242220.71875, 1242221.2607421875, 1242221.83203125, 1242222.103515625, 1242222.970703125, 1242223.849609375, 1242224.234375, 1242225.193359375,
    1242225.537109375, 1242226.345703125, 1242226.9990234375, 1242227.599609375, 1242227.978515625, 1242228.5849609375, 1242228.962890625, 1242229.291015625,
    1242229.8154296875, 1242230.1708984375, 1242230.630859375, 1242230.9794921875, 1242231.3359375, 1242231.7421875, 1242232.041015625, 1242232.517578125,
    1242232.93359375, 1242233.2890625, 1242233.6767578125, 1242234.0703125, 1242234.4638671875, 1242234.9033203125, 1242235.23828125, 1242235.625,
    1242236.0126953125, 1242236.28125, 1242236.6396484375, 1242237.56640625, 1242239.478515625, 1242240.4189453125, 1242241.388671875, 1242242.35546875,
    1242244.2861328125, 1242245.2841796875, 1242246.279296875, 1242247.2900390625, 1242248.3251953125, 1242249.36328125, 1242250.736328125, 1242251.0703125,
    1242251.1640625, 1242251.921875, 1242252.546875, 1242253.5751953125, 1242254.6064453125, 1242255.6201171875, 1242256.626953125, 1242257.568359375,
    1242258.5009765625, 1242259.509765625, 1242260.5712890625, 1242261.142578125, 1242261.66796875, 1242262.72265625, 1242263.7890625, 1242264.869140625,
    1242265.951171875, 1242266.9794921875, 1242268.0087890625, 1242269.0380859375, 1242270.046875, 1242271.0712890625, 1242272.162109375, 1242273.3310546875,
    1242274.494140625, 1242275.6552734375, 1242276.802734375, 1242277.8896484375, 1242278.9677734375, 1242280.048828125, 1242281.115234375, 1242282.1796875,
    1242283.25, 1242284.296875, 1242285.30859375, 1242286.3388671875, 1242287.40625, 1242288.45703125, 1242289.4921875, 1242290.5458984375,
    1242291.5986328125, 1242292.62109375, 1242293.65625, 1242294.6943359375, 1242295.7236328125, 1242296.7744140625, 1242297.849609375, 1242298.5556640625,
    1242299.51953125, 1242300.2177734375, 1242301.1015625, 1242302.2080078125, 1242303.3037109375, 1242304.3857421875, 1242305.453125, 1242306.4921875,
    1242307.544921875, 1242308.609375, 1242309.6494140625, 1242310.6845703125, 1242311.732421875, 1242312.775390625, 1242313.8115234375, 1242314.8408203125,
    1242315.859375, 1242316.9033203125, 1242317.9716796875, 1242319.04296875, 1242320.0966796875, 1242321.1630859375, 1242322.1953125, 1242323.2197265625,
    1242324.2373046875, 1242325.2265625, 1242326.1767578125, 1242327.123046875, 1242328.013671875, 1242328.6884765625, 1242329.87109375, 1242330.8564453125,
    1242331.814453125, 1242332.830078125, 1242333.8212890625, 1242334.83203125, 1242335.818359375, 1242336.8076171875, 1242337.78515625, 1242338.7470703125,
    1242339.7216796875, 1242340.6982421875, 1242341.6806640625, 1242342.6708984375, 1242343.666015625, 1242344.6630859375, 1242345.685546875, 1242346.7275390625,
    1242347.77734375, 1242348.791015625, 1242349.7216796875, 1242350.5986328125, 1242351.5146484375, 1242352.513671875, 1242353.6279296875, 1242354.7880859375,
    1242355.931640625, 1242357.0771484375, 1242358.205078125, 1242359.259765625, 1242360.314453125, 1242361.353515625, 1242362.4091796875, 1242363.470703125,
    1242364.474609375, 1242365.4462890625, 1242366.568359375, 1242367.7119140625, 1242368.8740234375, 1242369.982421875, 1242369.982421875, 1242369.982421875,
    1242371,
    1242372.0, 1242373.0419921875, 1242374.0595703125, 1242375.05078125, 1242376.0244140625, 1242376.9765625, 1242378.0068359375, 1242379.0810546875,
    1242380.2138671875, 1242381.3935546875, 1242382.5712890625, 1242383.7431640625, 1242384.8720703125, 1242385.97265625, 1242387.052734375, 1242388.087890625,
    1242389.091796875, 1242390.1025390625, 1242391.1162109375, 1242392.1533203125, 1242393.1689453125, 1242394.20703125, 1242395.2685546875, 1242396.3369140625,
    1242397.40625, 1242398.4853515625, 1242399.5390625, 1242400.5693359375, 1242401.5380859375, 1242402.552734375, 1242403.6220703125, 1242404.7431640625,
    1242405.86328125, 1242407.0126953125, 1242408.162109375, 1242409.2705078125, 1242410.3994140625, 1242411.5, 1242412.537109375, 1242413.5380859375,
    1242414.4072265625, 1242415.48046875, 1242416.5419921875, 1242417.6337890625, 1242418.68359375, 1242419.787109375, 1242420.8564453125, 1242421.9287109375,
    1242423.005859375, 1242424.02734375, 1242425.076171875, 1242426.12109375, 1242427.1767578125, 1242428.25, 1242429.3076171875, 1242430.3662109375,
    1242431.41015625, 1242432.4521484375, 1242433.4482421875, 1242434.455078125, 1242435.5009765625, 1242436.58984375, 1242437.6796875, 1242438.79296875,
    1242439.8974609375, 1242441.0107421875, 1242442.1044921875, 1242443.228515625, 1242444.3642578125, 1242445.474609375, 1242446.5673828125, 1242447.328125,
    1242448.6318359375, 1242449.6572265625, 1242450.7001953125, 1242451.7587890625, 1242452.8447265625, 1242453.94140625, 1242455.126953125, 1242456.3349609375,
    1242457.541015625, 1242458.7265625, 1242459.9248046875, 1242461.1240234375, 1242462.2998046875, 1242463.4736328125, 1242464.650390625, 1242465.81640625,
    1242466.9931640625, 1242468.1953125, 1242469.3505859375, 1242470.5322265625, 1242471.7412109375, 1242472.94140625, 1242474.1318359375, 1242475.3251953125,
    1242476.5107421875, 1242477.6181640625, 1242478.712890625, 1242479.8349609375, 1242480.9765625, 1242482.10546875, 1242483.21875, 1242484.33984375,
    1242485.396484375, 1242486.486328125, 1242487.6201171875, 1242488.7890625, 1242489.9208984375, 1242491.0703125, 1242492.2373046875, 1242493.4111328125,
    1242494.5732421875, 1242495.7470703125, 1242496.919921875, 1242498.0927734375, 1242499.2978515625, 1242500.4833984375, 1242501.65234375, 1242502.84765625,
    1242504.0380859375, 1242505.185546875, 1242506.326171875, 1242507.306640625, 1242508.5546875, 1242509.6640625, 1242510.7578125, 1242511.8408203125,
    1242512.943359375, 1242514.0673828125, 1242515.19921875, 1242516.3330078125, 1242517.4306640625, 1242518.533203125, 1242519.6357421875, 1242520.7138671875,
    1242521.80859375, 1242522.91015625, 1242523.9892578125, 1242525.08984375, 1242526.20703125, 1242527.3232421875, 1242528.4365234375, 1242529.53515625,
    1242530.6279296875, 1242531.673828125, 1242532.7119140625, 1242533.759765625, 1242534.8017578125, 1242535.83203125, 1242536.8779296875, 1242537.9150390625,
    1242538.9453125, 1242539.982421875, 1242540.98828125, 1242542.01171875, 1242543.0478515625, 1242544.1103515625, 1242545.2109375, 1242546.3203125,
    1242547.4580078125, 1242548.6123046875, 1242549.7822265625, 1242550.9775390625, 1242552.1669921875, 1242553.3349609375, 1242554.5078125, 1242555.6220703125,
    1242556.63671875, 1242557.666015625, 1242558.77734375, 1242559.89453125, 1242561.0458984375, 1242562.2314453125, 1242563.38671875, 1242564.5478515625,
    1242565.7177734375, 1242566.87109375, 1242568.041015625, 1242569.2255859375, 1242570.392578125, 1242571.5810546875, 1242572.79296875, 1242573.93359375,
    1242575.0634765625, 1242576.2080078125, 1242577.33203125, 1242578.447265625, 1242579.5517578125, 1242580.6748046875, 1242581.8388671875, 1242582.9521484375,
    1242584.0771484375, 1242585.220703125, 1242586.34375, 1242587.474609375, 1242588.6162109375, 1242589.7529296875, 1242590.9287109375, 1242592.11328125,
    1242593.3251953125, 1242594.53515625, 1242595.7724609375, 1242596.9892578125, 1242598.1728515625, 1242599.3134765625, 1242600.4345703125, 1242601.4814453125,
    1242602.4345703125, 1242603.390625, 1242604.404296875, 1242605.4287109375, 1242606.44921875, 1242607.4765625, 1242608.5234375, 1242609.35546875,
    1242609.8701171875, 1242610.9150390625, 1242611.9345703125, 1242612.939453125, 1242613.8974609375, 1242614.3642578125, 1242615.4052734375, 1242616.30078125,
    1242617.1884765625, 1242618.3427734375, 1242619.396484375, 1242619.9580078125, 1242621.015625, 1242621.939453125, 1242622.609375, 1242623.1474609375,
    1242623.92578125, 1242624.7041015625, 1242625.482421875, 1242626.5693359375, 1242627.5361328125, 1242628.419921875, 1242629.4208984375, 1242630.4853515625,
    1242631.486328125, 1242632.6103515625, 1242633.177734375, 1242633.8720703125, 1242634.8076171875, 1242635.220703125, 1242636.041015625, 1242636.732421875,
    1242637.4638671875, 1242638.1318359375, 1242638.765625, 1242639.2099609375, 1242639.8291015625, 1242640.5673828125, 1242640.9833984375, 1242641.58203125,
    1242642.1806640625, 1242642.6279296875, 1242643.330078125, 1242643.92578125, 1242644.515625, 1242645.1103515625, 1242645.5888671875, 1242646.17578125,
    1242646.74609375, 1242647.3330078125, 1242647.9072265625, 1242648.5498046875, 1242649.166015625, 1242649.681640625, 1242650.4130859375, 1242651.2177734375,
    1242651.8798828125, 1242652.744140625, 1242653.45703125, 1242654.244140625, 1242654.9755859375, 1242655.544921875, 1242656.203125, 1242656.8857421875,
    1242657.6220703125, 1242658.3173828125, 1242659.0693359375, 1242659.779296875, 1242660.4892578125, 1242661.1982421875, 1242662.560546875, 1242662.869140625,
    1242663.185546875, 1242663.560546875, 1242663.560546875, 1242663.560546875, 1242663.560546875, 1242663.560546875, 1242663.560546875, 1242663.560546875,
    1242959,
    1242960.0, 1242962.28515625, 1242963.3388671875, 1242964.3212890625, 1242965.3193359375, 1242966.2392578125, 1242967.150390625, 1242968.0263671875,
    1242969.041015625, 1242969.5400390625, 1242970.552734375, 1242971.1083984375, 1242972.1123046875, 1242973.158203125, 1242973.439453125, 1242973.9423828125,
    1242974.7841796875, 1242975.8095703125, 1242976.6220703125, 1242977.3203125, 1242978.3544921875, 1242979.2958984375, 1242980.1875, 1242981.12890625,
    1242982.130859375, 1242983.130859375, 1242984.1640625, 1242985.2080078125, 1242986.33203125, 1242987.5859375, 1242988.6240234375, 1242989.298828125,
    1242990.4794921875, 1242991.49609375, 1242992.0546875, 1242992.6044921875, 1242993.2138671875, 1242993.474609375, 1242994.2900390625, 1242994.9638671875,
    1242995.2333984375, 1242995.810546875, 1242996.0703125, 1242996.724609375, 1242997.26171875, 1242997.7607421875, 1242998.0234375, 1242998.400390625,
    1242998.8408203125, 1242999.455078125, 1242999.943359375, 1243000.59765625, 1243001.2041015625, 1243001.748046875, 1243002.2939453125, 1243002.8583984375,
    1243003.5771484375, 1243004.2158203125, 1243004.8154296875, 1243005.2958984375, 1243005.9736328125, 1243006.2998046875, 1243006.9052734375, 1243007.490234375,
    1243008.0478515625, 1243008.818359375, 1243009.2353515625, 1243009.9482421875, 1243010.71875, 1243011.47265625, 1243012.20703125, 1243012.9541015625,
    1243013.701171875, 1243014.4716796875, 1243015.236328125, 1243016.005859375, 1243016.6005859375, 1243017.5107421875, 1243018.248046875, 1243018.876953125,
    1243019.7783203125, 1243020.5439453125, 1243021.337890625, 1243022.1103515625, 1243022.931640625, 1243023.73046875, 1243024.5263671875, 1243025.3125,
    1243026.12890625, 1243026.6640625, 1243027.3427734375, 1243027.7578125, 1243028.578125, 1243029.4013671875, 1243030.1923828125, 1243031.0107421875,
    1243031.8251953125, 1243032.62890625, 1243033.40625, 1243034.197265625, 1243034.982421875, 1243035.8359375, 1243036.56640625, 1243037.3828125,
    1243038.197265625, 1243039.0830078125, 1243039.9013671875, 1243040.7587890625, 1243041.333984375, 1243042.330078125, 1243043.4169921875, 1243044.494140625,
    1243045.0302734375, 1243045.888671875, 1243046.4521484375, 1243047.0185546875, 1243047.5419921875, 1243048.1904296875, 1243048.619140625, 1243049.40234375,
    1243049.8798828125, 1243050.65625, 1243051.419921875, 1243052.0634765625, 1243052.9853515625, 1243053.783203125, 1243054.595703125, 1243055.4287109375,
    1243056.26171875, 1243057.1005859375, 1243057.92578125, 1243058.7275390625, 1243059.4921875, 1243060.2705078125, 1243061.0703125, 1243061.8583984375,
    1243062.6826171875, 1243063.5068359375, 1243064.3251953125, 1243065.146484375, 1243065.998046875, 1243066.880859375, 1243067.748046875, 1243068.626953125,
    1243069.509765625, 1243070.400390625, 1243071.251953125, 1243072.125, 1243072.984375, 1243073.86328125, 1243074.6982421875, 1243075.576171875,
    1243076.4404296875, 1243077.3369140625, 1243078.224609375, 1243079.2919921875, 1243079.97265625, 1243080.8681640625, 1243081.76953125, 1243082.71484375,
    1243083.6669921875, 1243084.6142578125, 1243085.5546875, 1243086.474609375, 1243087.390625, 1243088.2919921875, 1243089.197265625, 1243090.0693359375,
    1243090.9384765625, 1243091.8349609375, 1243092.751953125, 1243093.716796875, 1243094.640625, 1243095.576171875, 1243096.50390625, 1243097.400390625,
    1243098.2666015625, 1243099.16796875, 1243100.0771484375, 1243100.9423828125, 1243101.8251953125, 1243102.7099609375, 1243103.6357421875, 1243104.544921875,
    1243105.462890625, 1243106.357421875, 1243107.283203125, 1243108.162109375, 1243109.291015625, 1243109.92578125, 1243110.8173828125, 1243111.69921875,
    1243112.591796875, 1243113.484375, 1243114.3818359375, 1243115.3056640625, 1243116.1572265625, 1243117.0439453125, 1243117.9130859375, 1243118.759765625,
    1243119.619140625, 1243120.49609375, 1243121.3037109375, 1243122.15625, 1243122.9951171875, 1243123.8408203125, 1243124.6572265625, 1243125.5234375,
    1243126.4296875, 1243127.345703125, 1243128.24609375, 1243129.1162109375, 1243129.9873046875, 1243130.8427734375, 1243131.693359375, 1243132.537109375,
    1243133.392578125, 1243134.2099609375, 1243135.0498046875, 1243135.8857421875, 1243136.6962890625, 1243137.5595703125, 1243138.41015625, 1243139.1396484375,
    1243140.056640625, 1243141.23046875, 1243142.0625, 1243142.68359375, 1243143.3212890625, 1243144.1484375, 1243145.0078125, 1243145.8818359375,
    1243146.7666015625, 1243147.6484375, 1243148.5732421875, 1243149.482421875, 1243150.423828125, 1243151.373046875, 1243152.3349609375, 1243153.25,
    1243154.19140625, 1243155.1259765625, 1243156.0615234375, 1243157.0126953125, 1243157.9677734375, 1243158.9013671875, 1243159.8447265625, 1243160.779296875,
    1243161.6953125, 1243162.6357421875, 1243163.60546875, 1243164.5810546875, 1243165.5107421875, 1243166.4619140625, 1243167.3974609375, 1243168.33984375,
    1243169.1240234375, 1243170.2392578125, 1243171.1533203125, 1243172.0419921875, 1243172.9208984375, 1243173.6552734375, 1243174.66015625, 1243175.5439453125,
    1243176.466796875, 1243177.404296875, 1243178.35546875, 1243179.318359375, 1243180.25, 1243181.1796875, 1243182.0869140625, 1243183.0,
    1243183.9267578125, 1243184.849609375, 1243185.75, 1243186.6474609375, 1243187.546875, 1243188.4638671875, 1243189.3857421875, 1243190.2900390625,
    1243191.1982421875, 1243192.091796875, 1243192.978515625, 1243193.818359375, 1243194.638671875, 1243195.4541015625, 1243196.2802734375, 1243197.1318359375,
    1243198.0029296875, 1243198.8828125, 1243199.7529296875, 1243200.6591796875, 1243201.5380859375, 1243202.447265625, 1243203.3681640625, 1243204.236328125,
    1243205.1572265625, 1243206.103515625, 1243207.09765625, 1243208.09765625, 1243209.115234375, 1243210.1513671875, 1243211.1650390625, 1243212.1845703125,
    1243213.208984375, 1243214.201171875, 1243215.1787109375, 1243216.1171875, 1243217.0703125, 1243218.0224609375, 1243218.9775390625, 1243219.9580078125,
    1243220.9599609375, 1243221.953125, 1243222.8662109375, 1243223.7861328125, 1243224.69921875, 1243225.6396484375, 1243226.541015625, 1243227.4970703125,
    1243228.4462890625, 1243229.2880859375, 1243230.248046875, 1243231.1767578125, 1243232.1533203125, 1243233.0966796875, 1243234.033203125, 1243234.9755859375,
    1243235.919921875, 1243236.837890625, 1243237.71875, 1243238.6357421875, 1243239.5068359375, 1243240.43359375, 1243241.3515625, 1243242.26953125,
    1243243.107421875, 1243244.044921875, 1243244.9619140625, 1243245.94921875, 1243246.9560546875, 1243247.96484375, 1243249.080078125, 1243249.9404296875,
    1243250.89453125, 1243251.8291015625, 1243252.744140625, 1243253.6474609375, 1243254.55078125, 1243255.46484375, 1243256.3544921875, 1243257.2412109375,
    1243258.1591796875, 1243259.27734375, 1243260.03515625, 1243260.9609375, 1243261.9052734375, 1243262.791015625, 1243263.6513671875, 1243264.478515625,
    1243265.25, 1243266.01953125, 1243266.7841796875, 1243267.5302734375, 1243268.26953125, 1243269.0107421875, 1243269.751953125, 1243270.4755859375,
    1243271.1796875, 1243271.876953125, 1243272.5615234375, 1243273.2373046875, 1243273.9189453125, 1243274.591796875, 1243275.2490234375, 1243275.9033203125,
    1243276.595703125, 1243277.2861328125, 1243277.96484375, 1243278.626953125, 1243279.3115234375, 1243279.98046875, 1243280.6591796875, 1243281.3291015625,
    1243281.9873046875, 1243282.6435546875, 1243283.287109375, 1243283.9296875, 1243284.587890625, 1243285.2509765625, 1243285.904296875, 1243286.5712890625,
    1243287.228515625, 1243287.8857421875, 1243288.55859375, 1243289.1240234375, 1243289.76171875, 1243290.3994140625, 1243291.037109375, 1243291.6748046875,
    1243292.0361328125, 1243292.7470703125, 1243293.453125, 1243294.1689453125, 1243294.8798828125, 1243295.58203125, 1243296.2900390625, 1243296.9912109375,
    1243297.6904296875, 1243298.39453125, 1243298.39453125, 1243298.39453125, 1243298.39453125, 1243298.39453125, 1243298.39453125, 1243298.39453125,
]
