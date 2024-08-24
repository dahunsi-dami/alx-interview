#!/usr/bin/python3
"""Module containing validUTF8 method."""


def validUTF8(data):
    """Determines if given data set reps a valid UTF-8 encoding."""
    byte_count = 0

    for byte in data:
        # Use last 8 bits if byte passes 1 byte, e.g., 1024.
        # Doing bitwise & operation with byte achieves this.
        byte = byte & 0b11111111

        if byte_count == 0:
            # byte_count will store no. of leadings 1s in start byte.
            mask = 1 << 7
            while mask & byte:
                # That is, while mask & byte is not zero.
                byte_count += 1
                mask = mask >> 1

            # For a 1-byte char, byte_count will be properly 0.

            # If byte_count is 0, skip remaining code and go to-
            # -next iteration.
            if byte_count == 0:
                continue

            # Return False if count of bytes is invalid.
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            # This checks if next byte is a valid continuation byte.
            # Checks 1st byte is 1 and 2nd byte is 0.
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

        # Since we're working w/ multi-byte char at this point,
        # we need to decrease the byte count.

        # byte_count stores no. of bytes needed to complete the-
        # -character.

        # E.g., 110xxxxx is 2-byte char. byte_count is already 2.

        # Since we already have the 1st byte, we need 1 byte more-
        # -to complete the character, so we need to minus 1 to-
        # -show that we're looking for 1 more byte.
        byte_count -= 1

    # byte_count should be 0 if all bytes have been properly-
    # -processed.
    return byte_count == 0
