# Day 5: Code Implementation
# Log File Analyzer
# Write your implementation here independently.

total_line = 0
info_line = 0
warn_line = 0
errors = []

with open("app.log","r") as file:
    for line in file:
        total_line += 1
        clean_line = line.strip()
        if clean_line.startswith("[INFO]"):
            info_line +=1
        elif clean_line.startswith("[WARN]"):
            warn_line +=1 
        elif clean_line.startswith("[ERROR]"):
            errors.append(clean_line)

with open("summary.txt","w") as file:
    file.write("=== Log Analysis Summary === \n")
    file.write(f"Total lines Processed: {total_line} \n")
    file.write(f"INFO Count: {info_line} \n")
    file.write(f"WARN Count: {warn_line} \n")
    file.write(f"ERROR Count: {len(errors)} \n")
    file.write("---Error Details --- \n")
    for index,error_msg in enumerate(errors,start=1):
        file.write(f"{index}. {error_msg} \n")
print("Analysis complate! Saved to summary.txt")