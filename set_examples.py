bob_countries = ['China', 'Ecuador', 'Burkina Faso', 'China', 'China', 'Mexico', 'Spain', 'Portugal', 'Finland', 'Finland']

john_countries = ['Burkina Faso', 'China', 'France', 'Germany', 'Japan', 'France', 'France', 'Portugal',
                  'Finland', 'Sweden']

bob = set(bob_countries)
john = set(john_countries)
john.add('Austria')
john.add('Israel')
bob.add('China')
bob.add('Pakistan')
print("bob: {}".format(bob))
print("john: {}".format(john))

print("COMMON:", bob & john)  #  intersection
print("ONLY ONE:", bob ^ john)  # xor (AKA symmetric difference)
print("ALL:", bob | john)  # union
print("Only Bob:", bob - john)
print("Only John:", john - bob)
print()

unique_foods = set()
with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        unique_foods.add(food)
print("unique_foods: {}".format(unique_foods))
unique_foods.clear()

with open('DATA/breakfast.txt') as breakfast_in:
    unique_foods = set([line.rstrip() for line in breakfast_in])
print("unique_foods: {}".format(unique_foods))











