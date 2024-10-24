#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Function to print the statistics."""
    global total_size, status_codes_count
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle CTRL + C (SIGINT) signal to print stats."""
    print_stats()
    sys.exit(0)

# Set up signal handling for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Parse the log line
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract IP, date, method, URL, protocol, status code, and file size
            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        except (IndexError, ValueError):
            # If parsing fails, skip the line
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interrupt (CTRL + C)
    print_stats()
    sys.exit(0)
