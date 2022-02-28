actor = "Chris Hemsworth"

print(actor.upper())
print(actor.count('h'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'), actor.startswith('Liam'))
print("Chris" in actor, "Hem" in actor, "Haw" in actor)
# print(actor.__contains__("Chris"))  don't do this

s = "spam  \t  \n"
s2 = s.rstrip()
print(repr(s), repr(s2))

s3 = "      This is a test       "
print(repr(s3), repr(s3.strip()))

s4 = "My stuff...."
print(s4.rstrip('.'))

ip = "123.55.92.8"

print(ip.replace('.', ''))
print(ip.replace('.', '<=>'))

b = ip.split('.')
print(b)
print(",".join(b))
sep = "/"
print(sep.join(b))
print(", ".join(b))
print(" wombat ".join(b))

a = "foo"
b = "bar"
print(a + b)





