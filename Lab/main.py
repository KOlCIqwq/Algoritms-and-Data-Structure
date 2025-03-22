import matplotlib.pyplot as plt
from Algorithms.quick_sort_median import quick_sort_median
from Algorithms.quick_sort import quick_sort
from Algorithms.quick_sort_three import quicksort_3way
from Algorithms.counting_sort import counting_sort
from Algorithms.pigeonhole_sort import PigeonSort
from measure import get_Tmin, measure_time, geometric_progression

# Impostazioni degli esperimenti
samples = 100  # Numero di campioni
trials = 10    # Parametro per measure_time: il ciclo while esegue finché il tempo totale >= Tmin

# Calcola Tmin in base alla risoluzione del clock
Tmin = get_Tmin()
print(f"Tmin = {Tmin:.8f} s")

m_const = 100000  # Valore costante per m
n_values = geometric_progression(100, 100000, samples)

print(n_values)

times_quick_random = []
times_quick_median = []
times_quick_three = []
times_counting = []
times_pigeon = []

print("Esperimento 1: Variazione di n (m = 100000)")
for n in n_values:
    t_quick_random = measure_time(quick_sort, n, m_const, Tmin)
    t_quick_median = measure_time(quick_sort_median, n, m_const, Tmin)
    t_quick_three = measure_time(quicksort_3way, n, m_const, Tmin)
    t_counting = measure_time(counting_sort, n, m_const, Tmin)
    t_pigeon = measure_time(PigeonSort, n, m_const, Tmin)
    times_quick_random.append(t_quick_random)
    times_quick_median.append(t_quick_median)
    times_quick_three.append(t_quick_three)
    times_counting.append(t_counting)
    times_pigeon.append(t_pigeon)
    print(f"n = {n:6d} | Random: {t_quick_random:.8f} s | Median-of-Medians: {t_quick_median:.8f} s | Three-way: {t_quick_three:.8f} s | Counting: {t_counting:.8f} s | Pigeonhole: {t_pigeon:.8f} s")


