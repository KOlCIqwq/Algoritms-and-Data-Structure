import matplotlib.pyplot as plt
from Algorithms.quick_sort_median import quick_sort_median
from Algorithms.quick_sort import quick_sort
from measure import get_Tmin, measure_time, geometric_progression

# Impostazioni degli esperimenti
samples = 100  # Numero di campioni
trials = 10    # Parametro per measure_time: il ciclo while esegue finché il tempo totale >= Tmin

# Calcola Tmin in base alla risoluzione del clock
Tmin = get_Tmin()
print(f"Tmin = {Tmin:.8f} s")

##############################################
# Esperimento 1: Variazione di n con m costante
##############################################

m_const = 100000  # Valore costante per m
n_values = geometric_progression(100, 100000, samples)

times_random_n = []
times_median_n = []

print("Esperimento 1: Variazione di n (m = 100000)")
for n in n_values:
    t_random = measure_time(quick_sort, n, m_const, Tmin)
    t_median = measure_time(quick_sort_median, n, m_const, Tmin)
    times_random_n.append(t_random)
    times_median_n.append(t_median)
    print(f"n = {n:6d} | Random: {t_random:.8f} s | Median-of-Medians: {t_median:.8f} s")

