from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

## Zadanie 1: Implementacja równoważnego modelu w sklearn

# - Zaimplementuj model regresji liniowej za pomocą LinearRegression z sklearn.linear_model i porównaj jego wyniki z wynikami modelu PyTorch.
# - Przeprowadź trening i walidację modelu.
# - Porównaj metryki wydajności, takie jak MSE i R^2, dla obu modeli.

# Wskazówki:

# - Użyj metody fit na obiekcie LinearRegression do przeprowadzenia treningu.
# - Metoda score obiektu LinearRegression zwraca współczynnik determinacji R^2.
# - Możesz użyć mean_squared_error z sklearn.metrics do obliczenia MSE.
bias = 10
X_numpy, y_numpy, coef = make_regression(
    n_samples=5000,
    n_features=1,
    n_targets=1,
    noise=10,
    bias=bias,
    coef=True,
    random_state=42
)
model = LinearRegression()
model.fit(X_numpy, y_numpy)
y_pred = model.predict(X_numpy)
plt.scatter(X_numpy, y_numpy)
plt.plot(X_numpy, y_pred, color='red')
plt.show()