#!/usr/bin/python3
"""Log parsing module."""

import sys
import re
import signal


total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

log_pattern = re.compile(
        r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3})(?: (.*?))? (\d+)?$'
)


def print_stats():
    """
    Prints total file size & no. of occurrences-
    -of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles CTRL C interruption."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)

        if not match:
            continue

        ip, date, status_code, _unused, file_size = match.groups()

        if file_size and file_size.isdigit():
            total_size += int(file_size)

        status_code = int(status_code)
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
finally:
    print_stats()
