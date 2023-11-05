import numpy as np
import torch
import pandas as pd
import torch.nn as nn
import torch.optim as optim
import seaborn as sns
import matplotlib.pyplot as plt

#---take data
db = pd.read_csv('C:/Users/User/Desktop/programowanie/IdeaProjects/pyTorch/cz4/Iris.csv')
sns.set(style = 'ticks')

#---draw plot to figure out
# sns.pairplot(db, hue= 'Species')
# plt.show()

#---create variable to build tensor
petalWidthCm = db['PetalWidthCm'].values
species = db['Species'].values

#---Using LabelEncoder to convert species to integer labels
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X = torch.tensor(petalWidthCm, dtype=torch.float32)
Y = torch.tensor(label_encoder.fit_transform(species), dtype=torch.long)
iris_type = db['Species'].unique()
#---building model
model = nn.Sequential(
    nn.Linear(1, len(iris_type))
)

loss_fn   = nn.CrossEntropyLoss()  # Cross-Entropy Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)
n_epochs = 100
batch_size = 10

#... (pętla trenowania)
for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size].view(-1, 1)
        y_pred = model(Xbatch)
        ybatch = Y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Epoka {epoch}, funkcja straty {loss}')


with torch.no_grad():
    y_pred = model(X.view(-1, 1))
    predictions = torch.argmax(y_pred, dim=1)
accuracy = (predictions == Y).float().mean()

plt.show()
print(f"Accuracy {accuracy}")
