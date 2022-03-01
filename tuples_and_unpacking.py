
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person)
print(person[0], person[1])

first_name, last_name, product, dob = person  # iterable unpacking
print(first_name, last_name)

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

print(type(people), type(people[0]), type(people[0][0]))
print(people[0], people[0][0], people[0][0][0])

for first_name, last_name, *_ in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # first_name, last_name, product, dob = people[2]
    # etc
    print(first_name, last_name)
print('-' * 60)

values = [('a', 10), ('m', 19), ('z', 22), ('r', 24)]
for letter, number in values:
    print(letter, number)
print()







