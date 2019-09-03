import keras
import numpy as np


x = np.array([[5, 78, 2, 24, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])

y= np.array([[5, 78, 2, 24, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]])

keras.layers.Dense(512, activation='relu')
# output = relu(dot(W, input) + b)

def naive_relu(x):
    assert len(x.shape) == 2

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x
# i in x.shape=(3,5), Output: 3
# j in x.shape=(3,5), Output: 5
# x[3,5]=max(5,0) ??? x.shape[0]表示第一个轴上的多个元素？

def naive_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x

print(naive_relu(x))
print(naive_add(x, y))
