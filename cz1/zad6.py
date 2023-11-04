import torch
from torch import Tensor
import numpy as np
# Zadanie 6: Operacje macierzowe
# a) Oblicz iloczyn macierzowy (dot product) dwóch tensorów o odpowiednich rozmiarach.
# Twój kod tutaj
x = torch.tensor([[1, 2, 3],
                      [4, 5, 6]])
y = torch.tensor([[7, 8],
                      [9, 10],
                      [11, 12]])
resoult = torch.mm(x,y)
print(resoult)
# b) Transponuj tensor i wyjaśnij, jak zmienia się jego kształt.
# Twój kod tutaj
trans = resoult.transpose(0,1)
print(trans)