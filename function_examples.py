from math import pi

def get_message():
    return "Greetings, NNL world"

msg = get_message()
print(msg)

# def pi():
#     return 3.1417
#
# area = pi() * (5 ** 2)

def spam():
    pass

x = spam()
print(x)

def circle_area(diameter):
#    from math import pi
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

for d in nums:
    a = circle_area(d)
    print(f"diameter {d} area {a}")
print()

print(rectangle_area(5, 10))

def twice(x):
    return x * 2

print(twice(2), twice(10.5), twice('boo'), twice(['a', 'b', 'c']))


def outer():
    print("Hello from the outer function")
    inner()

def inner():
    print("Hello from the inner function")

outer()

def greet(whom="world"):
    print(f"Hello, {whom}")

greet('Mom')
greet('sailor')
greet("Dad")
greet()

animal = "walrus"   # GLOBAL scope   (actually file-global)

def spam():
    print("animal is", animal)
    city = "Troy"  # LOCAL variable
    return city

c = spam()
print(c)









