# Day 6: Main Entry Point
# Import analyzer and write execution logic here.

from analyzer import parse_logs

try:
    path = input("Enter log file path: ")
    result = parse_logs(path)
except FileNotFoundError:
    print(f"Error: the file {path} was not found.Plase check the path.")
except ValueError as e:
    print(f"Error: {e}")

else:
    print(result)