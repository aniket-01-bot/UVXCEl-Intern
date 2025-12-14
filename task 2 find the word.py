log_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\Gitdemo\\UVXCEl-Intern\\small.log"

word = input("Enter word to search: ")
count = 0

file = open(log_file, "r")

line_no = 1
for line in file:
    if word.lower() in line.lower():   
        print("Line", line_no, ":", line.strip())
        count = count + 1
    line_no = line_no + 1

file.close()

print("\nTotal matches:", count)
