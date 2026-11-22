# Day 22: Code Implementation
# NumPy Fundamentals: Vectorization vs Loops Benchmark & Broadcasting
# Write your implementations here independently.
import numpy as np
import time

def benchmark_vectorization(n=1000000):
    arr = np.random.rand(n)
    py_list = list(arr)
    start = time.perf_counter()
    cal_list = [x*2.5 + 10.0 for x in py_list]
    elapsed = time.perf_counter() - start
    start_again = time.perf_counter()
    num_list =arr*2.5+10.0
    elapsed_again = time.perf_counter() - start_again
    speedup = elapsed / elapsed_again
    print(f"NumPy was {speedup:.1f}x faster then python loop!")

def normalize_matrix_columns(matrix:np.ndarray)-> np.ndarray:
    col_means = matrix.mean(axis=0)
    return matrix - col_means


M = np.array([
    [10.0,20.0,30.0],
    [40.0,50.0,60.0],
    [70.0,80.0,90.0]
])

benchmark_vectorization()
print("Normalized Matrix:\n", normalize_matrix_columns(M))