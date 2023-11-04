import torch
from torch import Tensor
import numpy as np
# Zadanie 5: Operacje na tensorach i Numpy
# a) Utwórz tensor z listy Pythonowej i przekształć go w tablicę Numpy.
# Twój kod tutaj
lista = [1,2,3,4,5,6,7]
tensor = torch.tensor(lista)
tab_list = tensor.numpy()

# b) Zmień typ danych tensora z float na int i wyjaśnij obserwowane zmiany.
# Twój kod tutaj
x = torch.tensor([1.1, 2.2, 3.3, 4.4])
y = x.to(torch.int)
print(y)