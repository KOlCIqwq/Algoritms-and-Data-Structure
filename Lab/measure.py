import time
import math
import numpy as np
import random

def clock_resolution():
    '''
    Resolution time of pc
    '''
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start

def get_Tmin(E):
    R = clock_resolution()
    Tmin = R * (1/E + 1)
    return Tmin

def generate_array(n, m):
    # replace = False to generate unique elements
    arr = np.random.choice(np.arange(10, m + 1), size=n, replace=False).tolist()
    """ if repeated(arr):
        print("array contains repeated elements") """
    return arr
    
def repeated(arr):
    temp = set()
    for i in arr:
        if i in temp:
            return True
        temp.add(i)
    return False

def measure_init(n,m, Tmin):
    '''
    Calculate the time to generate an array of n elements with values from 1 to m.
    Purpose: We can generate different arrays for each sorting algorithm, or use the same, in case we use different arrays,
             we need to subtrack this initialization time from the total time.
    '''
    count = 0
    start_time = time.perf_counter()
    while True:
        generate_array(n,m)  # Uso una copia per non modificare l'array originale
        count += 1
        elapsed = time.perf_counter() - start_time
        if elapsed >= Tmin:
            break
    return elapsed / count

def main_measure(arr,sort_func, Tmin,n,m):
    '''
    Measure 10 times, get mean time
    '''
    times = [measure_time(arr, sort_func, Tmin, n, m) for _ in range(10)]
    return sum(times) / 10

def measure_time(arr,sort_func, Tmin,n,m):
    '''
    Proposed way to measure the time of a sorting algorithm.
    '''
    count = 0
    start_time = time.perf_counter()
    while True:
        #arr = generate_array(n,m)
        sort_func(arr.copy())  # Uso una copia per non modificare l'array originale
        count += 1
        elapsed = time.perf_counter() - start_time
        if elapsed >= Tmin:
            break
    #init = measure_init(n,m, Tmin)
    #return (elapsed - init) / count
    return elapsed / count

def geometric_progression(start, end, samples):
    # Proposed geometric sequence
    B = (end / start) ** (1 / (samples - 1))
    return [math.floor(start * (B ** i)) for i in range(samples)]

def generate_repeated(arr_size, n,m):
    '''
    Generate an array of size arr_size with n repeated n times.
    '''
    rep_elem = np.random.randint(10,m+1)
    arr = [rep_elem] * n
    arr.extend(generate_array(arr_size-n,m))
    random.shuffle(arr) # Shuffle the array to mix the repeated elements
    return arr

def reversed_sorted_array(n,m):
    '''
    Generate a reversed sorted array of size n with values from 1 to m.
    '''
    arr= generate_array(n,m)
    arr.sort(reverse=True)
    return arr
