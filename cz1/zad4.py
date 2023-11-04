import torch
from torch import Tensor
# Zadanie 4: Indeksowanie i wycinanie tensorów
# a) Wybierz z tensora elementy leżące na przekątnej macierzy (użyj tensora kwadratowego).
# Twój kod tutaj
x = torch.tensor([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
przekatna_macierzy = []
n = x.size(0)
for i in range(n):
    przekatna_macierzy.append(x[i,i])
print(przekatna_macierzy)

# b) Wyciągnij z tensora o kształcie (3, 4) drugi wiersz.
# Twój kod tutaj
x = torch.tensor([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
second = x[1, :]
print(second)

# c) Utwórz tensor (4, 4), a następnie wyciągnij z niego elementy, które znajdują się w parzystych kolumnach i nieparzystych wierszach.
# Twój kod tutaj
x = torch.tensor([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])
resoult = x[::2,1::2]
print(resoult)
