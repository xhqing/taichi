"""Count the number of primes in range [1, n].
"""
import time
import taichi as ti
ti.init()

@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n**0.5)+1):
        if n % k == 0: 
            result = False
            break
    return result

@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k): 
            count += 1
    return count

start_time = time.time()
print(count_primes(1000000))
end_time = time.time()
print("time cost: {}s".format(end_time-start_time))

