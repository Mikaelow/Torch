import torch
from torch import Tensor
import numpy as np
# Zadanie 8: Operacje w miejscu
# a) Przeprowadź dowolną operację arytmetyczną w miejscu (np. dodawanie) i zobacz, jak zmienia się tensor oryginalny.
# Twój kod tutaj
rowNb = 0
columnNb = 0
x = torch.tensor([[1, 2, 3],[4, 5, 6]])
while rowNb < x.size(0):
    while columnNb < x[rowNb].size(0):
        x[rowNb,columnNb] *= 2
        columnNb += 1
    columnNb=0
    rowNb += 1 
print(x)