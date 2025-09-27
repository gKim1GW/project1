import time, math

def run_2nd(n, a, b):   #project option 2
    sum_ = 0
    j = 2
    while j < n:
        k = 2                
        while k < n:
            idx = int(k)  # Convert k to int because list a, b indices must be integers
            sum_ += a[idx] * b[idx]
            k = k * math.sqrt(k)  
        j += j // 2             

# To reduce experimental noise, ran 999 trials for each n and used the median
def get_time(n, reps=999):
    times = []
    a = list(range(n)) # Size n is sufficient (k < n)
    b = list(range(n))
    for _ in range(reps):
        t1 = time.perf_counter_ns()
        run_2nd(n, a, b)
        t2 = time.perf_counter_ns()
        times.append(t2 - t1)
    times.sort()
    return times[len(times)//2]   

# n values to test
data_list = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for n in data_list:
    print(f"{n},{get_time(n)}")
