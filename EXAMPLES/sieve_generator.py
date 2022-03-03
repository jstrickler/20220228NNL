#!/usr/bin/env python

def next_prime(limit):
    flags = set()  # <1>

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # <2>
        yield i  # <3>


np = next_prime(200)  # <4>
print(np)
for prime in np:  # <5>
    print(prime, end=' ')
print('\n')

def suits():
    yield "Clubs"
    yield "Diamonds"
    yield "Hearts"
    yield "Spades"

suit_gen = suits()
for suit in suit_gen:
    print(suit)
print()

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip()

mary_in = trimmed('../DATA/mary.txt')
for line in mary_in:
    print(line)


#  x = [expr for var in iterable if condition]      x is a list
#  x = {expr for var in iterable if condition}      x is a set
#  x = (expr for var in iterable if condition)      x is a generator
#  x = {key:value for var in iterable if condition} x is a dictionary





