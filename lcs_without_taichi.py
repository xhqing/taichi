"""Longest Common Sequence
"""
import numpy as np
import time


benchmark = True

N = 15000

f = np.zeros(shape=(N+1, N+1), dtype=np.int32)

if benchmark:
    a_numpy = np.random.randint(0, 100, N, dtype=np.int32)
    b_numpy = np.random.randint(0, 100, N, dtype=np.int32)
else:
    a_numpy = np.array([0,1,0,2,4,3,1,2,1], dtype=np.int32)
    b_numpy = np.array([4,0,1,4,5,3,1,2], dtype=np.int32)

def compute_lcs(a, b):
    len_a, len_b = a.shape[0], b.shape[0]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            f[i, j] = max(f[i-1, j-1] + (a[i-1] == b[j-1]), max(f[i-1, j], f[i, j-1]))

    return f[len_a, len_b]

start_time = time.time()
print(compute_lcs(a_numpy, b_numpy))
end_time = time.time()
print("time cost: {}s".format(end_time-start_time))
