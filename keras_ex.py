import keras
import numpy as np
import pysnooper as ps


x = np.array([[5, 78, 2, 24, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])

y= np.array([[5, 78, 2, 24, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]])

keras.layers.Dense(512, activation='relu')
# output = relu(dot(W, input) + b)

@ps.snoop()
def naive_relu(x):
    assert len(x.shape) == 2

    # deep copy
    x = x.copy()
    # return range of index
    for i in range(x.shape[0]):
        # return range of index
        for j in range(x.shape[1]):
            # x[i, j], i and j are index
            x[i, j] = max(x[i, j], 0)
    return x

def naive_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape

    x = x.copy()
    for i in range(x.shape[0]):
        # print(i)
        for j in range(x.shape[1]):
            # print(x[i,j])
            x[i, j] += y[i, j]
    return x

print(naive_relu(x))
print(naive_add(x, y))
print(type(x.shape))
print(x.shape)
print(type(x))

z = x + y
z = np.maximum(z, 0.)
t = np.maximum(1., z)
print(z)
print(t)
# python3 keras_ex.py
