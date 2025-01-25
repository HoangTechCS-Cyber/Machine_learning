import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return torch.exp(x) / torch.exp(x).sum()


class softmax_stable(nn.Module):
    def __init__(self):
        super(softmax_stable, self).__init__()

    def forward(self, x):
       x_max = torch.max(x, dim=0, keepdims=True) 
       x_exp = torch.exp(x - x_max.values) 
       partition = x_exp.sum(0, keepdims=True) 
       return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)
# >> tensor ([0.0900 , 0.2447 , 0.6652])

data = torch.Tensor([1, 2, 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
print(output)
# >> tensor ([0.0900 , 0.2447 , 0.6652])
