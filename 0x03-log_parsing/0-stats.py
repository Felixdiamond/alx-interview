#!/usr/bin/python3
"""
This script reads from stdin line by line and computes the total file size
and the number of lines by status code. After every 10 lines and/or a keyboard
interruption (CTRL + C), it prints the statistics from the beginning.
The input format is `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>` and if the format is not this one, the line
is skipped. The possible status codes are 200, 301, 400, 401, 403, 404,
405 and 500. If a status code doesn’t appear or is not an integer,
nothing is printed for this status code. The status codes are
printed in ascending order.
"""

import sys

total_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_count = {code: 0 for code in status_codes}


def print_stats():
    """Prints the statistics from the beginning"""
    print("File size: {}".format(total_size))
    for code in status_codes:
        if status_count[code]:
            print("{}: {}".format(code, status_count[code]))


try:
    for count, line in enumerate(sys.stdin, 1):
        split_line = line.split()
        if len(split_line) < 2:
            continue
        try:
            size = int(split_line[-1])
            total_size += size
        except ValueError:
            pass
        try:
            status = int(split_line[-2])
            if status in status_codes:
                status_count[status] += 1
        except ValueError:
            pass
        if count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
