# Day 11: Code Implementation
# Generators, Lambdas, and High-Performance Stream Processing
# Write your implementation here independently.
import random 

def get_line():
    mode = ["[INFO]","[WARN]","[ERROR]"]
    range = 2000
    code = [404,403,500,502]
    ran_mode = random.choice(mode)
    ran_code = random.choice(code)
    ran_range = random.randint(0,2000)
    if ran_mode == "[ERROR]":
        return f"{ran_mode} Code:{ran_code} | Latency:{ran_range}ms \n"
    else:
        return f"{ran_mode} Latency:{ran_range}ms \n"

def create_mock_log(file_path, total_lines = 50):
    
    try:
        with open(file_path,'w') as file :
            for x in range(total_lines):
                line = get_line()
                file.write(line)
    except FileNotFoundError:
        print("File Not found")


# create_mock_log('app.log')

def stream_errors(file_path):
    try:
        with open(file_path,'r') as file:
            for line in file:
                clean_line = line.strip()
               
                if line.startswith("[ERROR]"):
                    raw_latency = clean_line.split("|")[1].split(":")[1]
                    latency = int(raw_latency.replace('ms',"").strip())
                    yield {"line":clean_line,"latency":latency}
                    
    except FileNotFoundError:
        print("File not Found")

def analyze_slowest_errors(file_path,top_n=3):
     items = stream_errors(file_path)
     sorted_items = sorted(items,key=lambda x:x["latency"],reverse=True)
     for i in range(0,3):
        print(sorted_items[i])

analyze_slowest_errors("app.log")