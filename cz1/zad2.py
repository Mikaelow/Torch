import torch
from torch import Tensor
# Zadanie 2: Operacje na tensorach
# a) Dodaj dwa tensory o tym samym kształcie i wypisz wynik.
# Twój kod tutaj

x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
# print(x+y)


# b) Przemnóż dwa tensory o kompatybilnych rozmiarach, wykorzystując mnożenie element po elemencie (element-wise).
# Twój kod tutaj

# print(x*y)


# c) Oblicz średnią i sumę elementów w tensorze.
# Twój kod tutaj

sumTensor = torch.sum(x)
print("Suma:", sumTensor)


x = x.float()
avgTensor = torch.mean(x)
print("Średnia:", avgTensor)

