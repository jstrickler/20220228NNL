#!/usr/bin/env python

ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print("{:.1f}\u00B0 C is {:.1f}\u00B0 F".format(c, f))

print()

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]


clean_fruits = [f.strip().lower() for f in fruits]
print(clean_fruits)
# print(', '.join(clean_fruits))
