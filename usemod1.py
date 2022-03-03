import sys
#     pkg.pkg  import module
#    john/math/geometry.py
from john.math import geometry

#  find and load geometry.py

c1 = geometry.circle_area(10)
c2 = geometry.circle_area(5.9)
r1 = geometry.rectangle_area(18, 26)
s1 = geometry.square_area(55)

print(c1, c2)
print(r1, s1)

print(geometry.ANIMAL)

# BAD PROGRAMMER! NO BISCUIT!!
geometry._helper()  # you COULD, but SHOULD you??

# module load priority
# 1. local folder
# 2. folders in PYTHONPATH
# 3. folders under sys.prefix
for path in sys.path:
    print(path)



