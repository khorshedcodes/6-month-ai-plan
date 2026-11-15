# Day 16: Asynchronous Python (`async` / `await` / `asyncio.gather`)

## Learning Objectives
1. Synchronous vs Asynchronous execution (I/O-bound tasks vs CPU-bound tasks).
2. The Python Event Loop (`asyncio.run()`).
3. Coroutines: `async def` and non-blocking suspension with `await`.
4. Concurrent batch execution with `asyncio.gather()`.
5. Comparing Python's `asyncio` to JavaScript's Event Loop and `Promise.all()`.

---

## Daily Task: Concurrent API Benchmarking Engine (Without AI)
Build a performance comparison script in `code.py`:
1. `simulate_network_fetch_sync(task_id: int, delay: float = 1.0) -> str`:
   - Simulates a blocking API call using `time.sleep(delay)`.
   - Runs 4 tasks sequentially and measures total time (takes ~4.0 seconds).
2. `simulate_network_fetch_async(task_id: int, delay: float = 1.0) -> str`:
   - An `async def` coroutine simulating non-blocking network fetch using `await asyncio.sleep(delay)`.
3. `run_concurrent_batch()`:
   - Uses `asyncio.gather(*tasks)` to execute all 4 requests concurrently.
   - Measures total time (takes ~1.0 second!).
4. Compare and print the speedup factor (`sync_time / async_time`)!

---

## Developer English Task: Technical Comparison
Write 3-4 professional sentences comparing Python's `asyncio` to JavaScript's `async/await` and `Promise.all()`.
