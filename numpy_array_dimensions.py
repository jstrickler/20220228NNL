import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6])
print("a1: \n{}".format(a1))
print("a1.shape: {}\n".format(a1.shape))

a1.shape = 3, 2
print("a1: \n{}".format(a1))
print("a1.shape: {}\n".format(a1.shape))

a1.shape = 6, 1
print("a1: \n{}".format(a1))
print("a1.shape: {}\n".format(a1.shape))

a1.shape = 1, 6
print("a1: \n{}".format(a1))
print("a1.shape: {}".format(a1.shape))
