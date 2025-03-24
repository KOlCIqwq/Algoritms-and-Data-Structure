import matplotlib.pyplot as plt
from Algorithms.quick_sort_median import quick_sort_median
from Algorithms.quick_sort import quick_sort
from Algorithms.quick_sort_three import helper
from Algorithms.counting_sort import counting_sort
#from Algorithms.pigeonhole_sort import PigeonSort
from Algorithms.RadixSort import RadixSort
from measure import get_Tmin, measure_time, geometric_progression, generate_array

samples = 200  # Numero di campioni

Tmin = get_Tmin(samples)
print(f"Tmin = {Tmin:.8f} s")

M = 100000
n_values = geometric_progression(100, 100000, samples)
times_quick_random = []
times_quick_median = []
times_quick_three = []
times_counting = []
#times_pigeon = []
times_radix = []

for n in n_values:
    # Generate only 1 array for all sorting algorithms
    arr = generate_array(n, M)
    # Get time for each sorting algorithm
    t_quick_random = measure_time(arr,quick_sort, Tmin,n,M)
    t_quick_median = measure_time(arr,quick_sort_median, Tmin,n,M)
    t_quick_three = measure_time(arr,helper, Tmin,n,M)
    t_counting = measure_time(arr,counting_sort, Tmin,n,M)
    #t_pigeon = measure_time(arr,PigeonSort, Tmin,n,M)
    t_radix = measure_time(arr,RadixSort, Tmin,n,M)
    # Save to log
    times_quick_random.append(t_quick_random)
    times_quick_median.append(t_quick_median)
    times_quick_three.append(t_quick_three)
    times_counting.append(t_counting)
    #times_pigeon.append(t_pigeon)
    times_radix.append(t_radix)
    # Print time for check
    print(f"n = {n:6d} | Random: {t_quick_random:.8f} s | Median-of-Medians: {t_quick_median:.8f} s | Three-way: {t_quick_three:.8f} s | Counting: {t_counting:.8f} s | Pigeonhole: {t_radix:.8f} s")
#n_values.insert(0,0)

