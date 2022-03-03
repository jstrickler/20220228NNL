from math import pi

_my_data = 1234

ANIMAL = 'wombat'

def main():
    print("Are we having fun yet?")
    c = circle_area(5)
    r = rectangle_area(5, 8)
    print(c, r)

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return rectangle_area(length, length)

def _helper():
    print("I am helping??")

if __name__ == '__main__':  # if I'm a script, not a module
    main()