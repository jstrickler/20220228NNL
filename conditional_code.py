#  if and friends
#  while loop

value = 56

if value > 75:
    print("Kangaroo")
    print("Koala")
    print("Kookaburra")
elif value > 50:
    print("wombat")
    print("wallaby")
elif value > 25:
    print("Quokka")
    print("cane toad")
else:
    print("blue-ringed octopus")

if value:    # if bool(value) == True
    print("Wahoooooooo")

print("All done.")

value = input("Enter True or False: ")
if value.lower().startswith('t'):
    token = True
elif value.lower().startswith('f'):
    token = False
else:
    print("please enter 't' or 'f'")

# x is False if:
#  x == 0     x == None     x == False
#  len(x) == 0

# value =  A ? B : C

debug = True

color = "red" if debug else "green"

print("color:", color)

# == != > < >= <=









