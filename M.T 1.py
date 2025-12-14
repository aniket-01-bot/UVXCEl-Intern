log_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\uvXcel\\task-1\\task-1\\medium.log"

InfoCount = 0
WarnCount = 0
ErrorCount = 0
Total = 0

with open(log_file, "r") as f:
    for line in f:
        Total += 1
        line_upper = line.upper()

        if "INFO" in line_upper:
            InfoCount += 1
        elif "WARN" in line_upper:
            WarnCount += 1
        elif "ERROR" in line_upper:
            ErrorCount += 1

print("Total entries:", Total)
print("INFO:", InfoCount)
print("WARN:", WarnCount)
print("ERROR:", ErrorCount)
