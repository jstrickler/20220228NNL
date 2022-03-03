#!/usr/bin/env python
import numpy as np

a1 = np.arange(15)  # <1>
print("a1 shape", a1.shape)  # <2>
print()

a1.shape = 15, 1
print("a1 (15, 1):", a1)

print(a1)
print()

a1.shape = 3, 5  # <3>
print(a1)
print()

a1.shape = 5, 3  # <4>
print(a1)
print()

print(a1.flatten())  # <5>
print()

f = a1.flatten()
print("shape of flat array:", f.shape)

print(a1.transpose())  # <6>
print("------------------")

a2 = np.arange(40)  # <7>
a2.shape = 2, 5, 4  # <8>

print(a2)
print()
