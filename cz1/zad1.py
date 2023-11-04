import torch
from torch import Tensor

# Zadanie 1: Tworzenie tensorów
# a) Utwórz tensor wypełniony zerami o rozmiarze (5, 3).
# Twój kod tutaj
x = torch.zeros(2, 3)
print(x)

# b) Utwórz tensor wypełniony jedynkami o dowolnym rozmiarze wybranym przez siebie.
# Twój kod tutaj
x = torch.ones(2,3)
print(x)


# c) Utwórz tensor wypełniony sekwencją liczb całkowitych od 10 do 19.
# Twój kod tutaj
x= torch.arange(10,20)
print(x)

