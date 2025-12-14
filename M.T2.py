log_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\uvXcel\\task-1\\task-1\\medium.log"

search_text = input("Enter text to search in log file: ").strip().lower()

count = 0

file = open(log_file, "r")

line_no = 1
for line in file:
    if search_text in line.lower():   # case-insensitive search
        print("Line", line_no, ":", line.strip())
        count = count + 1
    line_no = line_no + 1

file.close()

print("\nTotal matches:", count)
