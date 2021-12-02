import torch.nn
import torchvision

# train_set = torchvision.datasets.MNIST(root='../dataset/mnist', train=True, download=True)
# test_set = torchvision.datasets.MNIST(root='../dataset/mnist', train=False, download=True)

# 1.Prepare dataset
x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[0], [0], [1]])


# 2.Design model using Class
class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred


model = LogisticRegressionModel()

# 3.Construct loss and optimizer
criterion = torch.nn.BCELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4.Training cycle
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
