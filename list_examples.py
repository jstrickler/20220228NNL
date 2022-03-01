import sys


list1 = list()
list2 = []

list3 = ['red', 'purple', 'orange', 'white', 'tan']

cities = ['Albany', 'McKeesport', 'Colonie', 'Homestead', 'Pittsburgh', 'Saratoga Springs']

print(cities)
print(len(cities))

cities.insert(0, "Schenectady")
cities.insert(3, 'Niskayuna')
print(cities)
cities.append("Boston")
cities.append("Sewickley")
print(cities)

more_cities = ['Durham', 'Raleigh', 'Charlotte']
cities.extend(more_cities)
print(cities)

#  LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[8]
print(cities)

pos = cities.index('Sewickley')
print(pos)
del cities[8]
print(cities)

c = cities.pop()
print(c)
print(cities)

c = cities.pop(0)
print(c)
print(cities)

cities.remove('Pittsburgh')
print(cities)

#  del LIST[pos]    LIST.pop(pos=-1)   LIST.remove(value)
print(cities[0], cities[4], cities[-1], cities[-2], cities[len(cities) - 1])

print(cities[0:4])
print(cities[:4])

#   [start:stop]  [:stop]    [start:]   [start:stop:step]
print(cities[:])
print(cities[::])
print(cities[::2])
print(cities[::3])
print(cities[3:6])
print(cities[3:5])
print(cities[3:20])
print(cities[3:])
print(cities[-3:])

s = "John Smith"
print(s[:4])
print(s[-5:])
print(s[1:3])
print(s[6:9])
print()

for city in cities:
    #  city = cities[0]
    #  city = cities[1]
    #  ...
    print(city)
print(city)
print()

for char in s:
    print(char)
print()

print(list(s), '\n')

values = ['a', 'b', 'c', 'd', 'e']
for value in values:
    print(value)
    if value == 'c':
        break

for value in value[1:]:
    print(value)

for file_path in sys.argv[1:]:
    print(file_path)
















