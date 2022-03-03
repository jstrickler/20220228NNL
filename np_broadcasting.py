
import numpy as np

a = np.array(
    [[70, 31, 21, -76, 19, 5, 54, 66],
     [23, 29, -71, 12, 27, 74, 65, 73]], dtype=np.ushort)  # <1>

b = np.array(
    [[11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90]]
)  # <2>

print(np.multiply(a, b))  # a * b

print(np.negative(a))

b.shape = 8, 2
print(np.dot(a, b))

print(a @ b)

def spam(x):
    return 1000 * x

print(spam(a))

#  a.__rmul__(a, rmul, 1000)


