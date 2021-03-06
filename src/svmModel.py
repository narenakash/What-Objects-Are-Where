import torch
import torch.nn as nn

class SVM(nn.Module):
    def __init__(self):
        super().__init__()
        self.fully_connected = nn.Linear(1000, 1)

    def forward(self, x):
        output = self.fully_connected(x)
        return output
