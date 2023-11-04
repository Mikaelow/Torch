import numpy as np

def analiza_macierzy(macierz):
    """
    Ta funkcja zwraca średnią, maksymalną i minimalną wartość elementów macierzy.

    Parametry:
    macierz (np.array): Macierz NumPy do analizy.

    Zwraca:
    tuple: Trójka zawierająca średnią, maksymalną i minimalną wartość.
    """
    # Twoje rozwiązanie tutaj
    maxMacierz = np.max(macierz)
    minMacierz = np.min(macierz)
    avgMacierz = np.mean(macierz)
    return maxMacierz, minMacierz, avgMacierz
    
# Przykładowe dane wejściowe
macierz_przykladowa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Wywołanie funkcji
print(analiza_macierzy(macierz_przykladowa))
