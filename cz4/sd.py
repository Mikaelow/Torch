import torch  # Importowanie biblioteki PyTorch
import torch.nn as nn  # Importowanie modułu do tworzenia sieci neuronowych
import torch.optim as optim  # Importowanie modułu do optymalizacji
import torchvision  # Importowanie biblioteki torchvision

transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])

trainset = torchvision.datasets.FER2013(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.FER2013(root='./data', train=False, download=True, transform=transform)