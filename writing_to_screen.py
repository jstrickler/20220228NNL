import sys

person = "Fred Flintstone"
city = "Bedrock"
value = 43.38923892

print(person, city, value)
# write str(person) + ' ' + str(city) + ' ' + str(value) + '\n' to STDOUT

print(person, city, value, sep="/")
print(person, city, value, sep=" BAZINGA! ")
print(person, city, value, sep="")

print(person, end=' ')
print(city)
print("OK")

print(person, end='')
print(city, end='')
print(value)

# print(person, city, value, end='\n', sep=' ', file=sys.stderr)

print(person, "lives in", city)
print(f"{person} lives in {city}")   # 3.6 and later
print(f"2 + 2 is {2 + 2}")
print("{} lives in {}".format(person, city))

print(f"value is {value:.2f}")  # NEW
print("value is {:.2f}".format(value))  # OLD

print("value is %.2f" % (value))  # MORE OLD

values = [1.239039023, 9.3792749274, 14.8283]
for v in values:
    print(f"{v:.2f}")

formatted_values = [f"{v:.1f}" for v in values]
print(formatted_values)



