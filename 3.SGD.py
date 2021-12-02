import matplotlib.pyplot as plt
import numpy as np

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0


def forward(x):
    return x * w


def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2


def gradient(x, y):
    return 2 * x * (x * w - y)


print('Predict (before training)', 4, forward(4))
for epoch in range(10):
    for x, y in zip(x_data, y_data):
        cost = loss(x, y)
        grad = gradient(x, y)
        w -= 0.01 * grad
    print('Epoch:', epoch, 'w=', w)
print('Predict (after training)', 4, forward(4))

# plt.plot(epoch_list, cost_list)
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.show()
