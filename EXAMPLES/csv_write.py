#!/usr/bin/env python
import sys
import csv

data = [
    ('February', 28, 'The shortest month, with 28 or 29 days'),
    ('March', 31, 'Goes out like a "lamb"'),
    ('April', 30, 'Its showers bring May flowers'),
]

with open('../TEMP/stuff.csv', 'w') as stuff_in:
    if sys.platform == 'win32':
        wtr = csv.writer(stuff_in, lineterminator='\n') # <1>
    else:
        wtr = csv.writer(stuff_in) # <1>
    for row in data:
        wtr.writerow(row) # <2>

with open('../DATA/columns_of_numbers.txt') as col_in:
    with open('columns.csv', 'w') as col_out:
        wtr = csv.writer(col_out, lineterminator='\n')
        for row in col_in:
            fields = row.rstrip().split()
            wtr.writerow(fields)

with open('columns.csv') as col_in:
    rdr = csv.DictReader(col_in)
    for row in rdr:
        print(row['Alpha'], row['Gamma'])