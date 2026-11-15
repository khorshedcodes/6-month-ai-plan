# Day 16: Code Implementation
# Asynchronous Python: asyncio, coroutines, and concurrent batching
# Write your synchronous vs asynchronous benchmarks here independently.
import time
import asyncio

def simulate_sync_fetch(task_id:int,delay:float=1.0)->str:
    time.sleep(delay)
    return f"Sync Data #{task_id}"

def run_sync_benchmark(num_tasks=4):
    start = time.perf_counter()
    for task in range(1,num_tasks+1):
        simulate_sync_fetch(task)
    elapsed_sync = time.perf_counter() - start
    print(f"[SYNC] Finished {num_tasks} tasks in {elapsed_sync:.2f}s")
    return elapsed_sync

async def simulate_async_fetch(task_id:int,delay:float=1.0)-> str:
    await asyncio.sleep(delay)
    return f"Async Data #{task_id}"

async def run_async_benchmark(num_tasks=4):
    start = time.perf_counter()
    tasks = [simulate_async_fetch(i) for i in range(1,num_tasks+1)]
    results = await asyncio.gather(*tasks)
    elapsed_async = time.perf_counter() - start
    print(f"[Async] Finished {num_tasks} task in {elapsed_async:.2f}s")
    return elapsed_async


elapsed_sync = run_sync_benchmark()
elapsed_async = asyncio.run(run_async_benchmark())
speedup = elapsed_sync/elapsed_async
print(f"Speedup: Async was {speedup:.1f}x faster then sync!")