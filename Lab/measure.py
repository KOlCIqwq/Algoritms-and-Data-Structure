import time
import math
import numpy as np

def clock_resolution():
    """
    Calcola la risoluzione del clock utilizzando time.perf_counter().
    """
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start

def get_Tmin():
    """
    Calcola Tmin = R * 10, dove R è la risoluzione del clock.
    """
    R = clock_resolution()
    Tmin = R * 10
    return Tmin

def measure_time(sort_func, n, m, Tmin):
    """
    Esegue sort_func ripetutamente su array generati casualmente di dimensione n
    con interi in [1, m] finché il tempo totale misurato è >= Tmin.
    Restituisce il tempo medio per singola esecuzione.
    """
    count = 0
    start_time = time.perf_counter()
    while True:
        arr = np.random.randint(1, m + 1, size=n).tolist()
        sort_func(arr.copy())  # Uso una copia per non modificare l'array originale
        count += 1
        elapsed = time.perf_counter() - start_time
        if elapsed >= Tmin:
            break
    return elapsed / count

def geometric_progression(start, end, samples):
    """
    Restituisce una lista di valori interi in progressione geometrica.
    """
    B = (end / start) ** (1 / (samples - 1))
    return [math.floor(start * (B ** i)) for i in range(samples)]
