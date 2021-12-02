import torch

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])


class LinearMode(torch.nn.Module):
    def __init__(self):
        super(LinearMode, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


model = LinearMode()
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(f'w = {model.linear.weight.item()}')
print(f'b = {model.linear.bias.item()}')

x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print(f'y_pred = {y_test.item()}')

