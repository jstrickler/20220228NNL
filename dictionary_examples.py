
d1 = dict() 
d2 = {}

d3 = {
    'EXAMPLES': ['foo.py', 'bar.py'], 
    'ANSWERS': ['spam.py', 'ham.py'],
}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
    'LAX': 'Los Angeles',
}

airports['PIT'] = 'Pittsburgh'
airports['ALB'] = 'Albany'
airports['ALB'] = 'Colonie'
print("airports: {}".format(airports))

print(airports['YYZ'])
print(airports['SJC'])
print(airports.get('PSP'))
print(airports.get('PSP', 'NOT FOUND'))

print(airports.setdefault('PSP', 'Palm Springs'))
print(airports)

del airports['MCI']
print(airports)

print(len(airports))
print(airports.keys())
print(airports.values())
print()

for abbr in 'RDU', 'UVX', 'Zombieland', 'LAX', 'ALB', 'YYK', 'PSP':
    print(abbr, end=' ')
    if abbr in airports:
        print("YES", end='')
    else:
        print("NO", end='')
    print()
print()

for abbr, city in airports.items():
    print(abbr, city)
print()

for abbr, city in sorted(airports.items()):
    print(abbr, city)
print()

print(airports.items(), '\n')













