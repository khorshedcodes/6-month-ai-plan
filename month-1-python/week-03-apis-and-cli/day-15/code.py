# Day 15: Code Implementation
# Production Decorators: @timer and @retry
# Write your decorators and test functions here independently.
import functools 
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"[BENCHMARK] {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

def retry(max_attempts=3,delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(1,max_attempts+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt == max_attempts:
                        raise e
                time.sleep(delay)
        return wrapper
    return decorator


@timer
def process_numbers(n):
    total =sum(i*i for i in range(n))
    print(total)

attempts_count = 0

@retry(max_attempts=3, delay=1)
def unstable_network_call():
    global attempts_count
    attempts_count +=1 
    if attempts_count < 3:
        raise ConnectionError("Network timeout")
    print("Success! Data recived.")
    print("Ok")


print("--- Testing @timer ---")
process_numbers(10000)

print("\n--- Testing @retry ---")
unstable_network_call()