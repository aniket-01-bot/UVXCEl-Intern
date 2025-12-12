import re
from datetime import datetime
from collections import defaultdict

log_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\Gitdemo\\UVXCEl-Intern\\small.log"

# Counters check the log levels
info_count = 0
warn_count = 0
error_count = 0
total = 0

# Time tracking variables time range
start_time = None
end_time = None
time_pattern = r"\[(.*?)\]"

# Error count per hour dictionary initialization 
errors_by_hour = defaultdict(int)# Default dictionary to hold error counts per hour

with open(log_file, "r") as f:# Open the log file for reading
    for line in f:
        total += 1
        line_upper = line.upper()

        # Count log levels checks the info warn error occurrences
        if "INFO" in line_upper:
            info_count += 1
        if "WARN" in line_upper:
            warn_count += 1
        if "ERROR" in line_upper:
            error_count += 1

        # Extract timestamps and track time range
        match = re.search(time_pattern, line)
        if match:
            timestamp_str = match.group(1)
            ts = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")# Convert string to datetime object

            # Track start/end timestamps for time range
            if start_time is None:
                start_time = ts
            end_time = ts

            # Track error per hour counts for error distribution
            if "ERROR" in line_upper:
                hour = ts.strftime("%H")  # it can extracts  the hour part in 24-hour format
                errors_by_hour[hour] += 1

# -------- OUTPUT --------
print("Summary")
print("-------")
print(f"Total entries: {total}")
print(f"INFO: {info_count}")
print(f"WARN: {warn_count}")
print(f"ERROR: {error_count}\n")

print("Time Range:")
print(f"{start_time} → {end_time}\n")

print("Errors per hour:")
for hour in sorted(errors_by_hour.keys()):
    print(f"{hour}: {errors_by_hour[hour]} errors")
