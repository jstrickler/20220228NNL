
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), min(fruits), max(fruits))
print(len(nums), min(nums), max(nums), sum(nums))
print(sorted(fruits))
print(sorted(nums))
print('-' * 60)

reversed_fruits = reversed(fruits)
print(reversed_fruits)
for fruit in reversed_fruits:
    print(fruit)
print('-' * 60)

states = ['PA', 'NC', 'CA', 'TX', 'NY', 'ID']
capitals = ['Harrisburg', 'Raleigh', 'Sacramento', 'Austin', 'Albany', 'Boise']

state_capitals = zip(states, capitals)
print("state_capitals: {}".format(state_capitals))
print(list(state_capitals))
state_capitals = zip(states, capitals)
for state, capital in state_capitals:
    print(state, capital)
print('-' * 60)

e = enumerate(states)
print(list(e))
e = enumerate(states)
for i, value in e:
    print(i, value)
print()

#  range(stop)  range(start, stop)   range(start, stop, step)
for i in range(5):   # range(0, 5)
    print("Python is the best!")
print()

for i in range(1, 11):
    print(i, end=' ')
print('\n')

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']

first_half = 'foo'
second_half = 'bar'

print(x + y, first_half + second_half)
print('-' * 60)

print('0' * 5)
print("WOMBAT COMBAT! " * 3)

flags = [False] * 10
print("flags: {}".format(flags))

print([1, 2, 3] * 5)

print([0] * 25)













