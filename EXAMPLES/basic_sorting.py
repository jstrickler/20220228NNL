#!/usr/bin/env python

"""Basic sorting example"""

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruit)  # <1>

print(sorted_fruit, '\n')

f2 = sorted(fruit, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruit, key=len)   # len is a callback here
print("f3: {}\n".format(f3))

def sort_fruits(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruit, key=sort_fruits)
print("f4: {}\n".format(f4))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(p):
    return p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[-1]):
    print(person)
print()
#   lambda parameter-list: return-value

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()
