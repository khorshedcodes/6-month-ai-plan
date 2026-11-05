# Day 6: Log Analyzer Module
# Write your helper functions here.

def parse_logs(file_path):
    total_line = 0
    info_total = 0
    warn_total = 0 
    error = []

    with open(file_path,"r") as file:
       for line in file:
        total_line += 1
        clean_line  = line.strip()
        if clean_line.startswith("[INFO]"):
            info_total += 1
        elif clean_line.startswith("[WARN]"):
            warn_total += 1
        elif clean_line.startswith("[ERROR]"):
            error.append(clean_line)
    if total_line == 0:
        raise ValueError("log file is empty!")
    return {
        "total":total_line,
        "info":info_total,
        "warn":warn_total,
        "error":len(error),
        "errors_list":error
        }