import re

log_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\Gitdemo\\UVXCEl-Intern\\small.log"

# Take user input to search (case insensitive)
search_text = input("Enter text to search in log file: ").strip().lower()

match_count = 0
matching_lines = []

with open(log_file, "r") as f:
    for line_number, line in enumerate(f, start=1):
        # Case-insensitive search
        if search_text in line.lower():
            match_count += 1
            matching_lines.append((line_number, line.strip()))

print("\nMatching Lines")#Print Each Matching Line 
print("---------------")
for ln, text in matching_lines:
    print(f"Line {ln}: {text}")#in stands for line number and text

print("\nTotal Matches Found:", match_count)# gives the total number of matches found
