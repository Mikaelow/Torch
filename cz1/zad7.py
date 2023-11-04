import torch
from torch import Tensor
import numpy as np
# Zadanie 7: Zaawansowane indeksowanie
# a) Użyj maski logicznej, aby wybrać z tensora tylko te elementy, które są większe od średniej wartości wszystkich elementów w tensorze.
# Twój kod tutaj
x = torch.tensor([[1, 2, 3],[4, 5, 6]])
x = x.float()
avgX = torch.mean(x)
wieksze_od_sr = []
for row in x:
    for i in row:
        if i > avgX:
            wieksze_od_sr.append(i)
        else: pass
print(wieksze_od_sr)

# b) Wybierz z tensora elementy, które są parzyste i zastąp je wartością -1.
# Twój kod tutaj
rowNb = 0
columnNb=0
while rowNb < x.size(0):
    while columnNb < x[rowNb].size(0):
        if x[rowNb,columnNb]%2 == 0:
            x[rowNb,columnNb]=-1
        else: pass
        columnNb += 1
    columnNb=0
    rowNb += 1 
print(x)
