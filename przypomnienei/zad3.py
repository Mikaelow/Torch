# Zadanie 3: Wizualizacja danych z Matplotlib
# Korzystając z biblioteki Matplotlib, stwórz wykres funkcji sinus i cosinus na jednym wykresie.
# Oś X powinna reprezentować wartości od 0 do 4π, a oś Y wartości funkcji.
# Dodaj legendę, tytuł wykresu oraz etykiety osi.


import matplotlib.pyplot as plt
import numpy as np
# uyzj np.linspace i np.pi do wygenerowania wartości X
# np.sin i np.cos do wygenerowania wartości Y
x = np.linspace(0,100,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()
# Twoje rozwiązanie tutaj