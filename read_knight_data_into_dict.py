from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data.setdefault(name, (title, color, quest, comment))
        # knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for knight, data in knight_data.items():
    print(data[0], knight, data[2])
print()

print(knight_data['Robin'][3])
print(knight_data['Bedevere'][1])


