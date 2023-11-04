import torch
from torch import Tensor
# Zadanie 3: Zmiana kształtu tensorów
# a) Zmień kształt jednego z wcześniej utworzonych tensorów na kształt (3, 5).
# Twój kod tutaj
x = torch.tensor([[1, 2], [3, 4]])
x = x.view(4, 1)
print(x)


# b) Spłaszcz tensor o dowolnym kształcie do jednowymiarowego tensora i wypisz jego zawartość.
# Twój kod tutaj
x = x.view(1, 4)
print(x)