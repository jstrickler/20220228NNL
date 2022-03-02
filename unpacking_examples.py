

values = ['a', 'b', 'c', 'd', 'e', 'f']

#   var, ... = iterable
a1, a2, a3, a4, a5, a6 = values
print(a1, a2, a3, a4, a5, a6, '\n')

a1, a2, *a3 = values
print(a1, a2, a3)

a1, *a2, a3 = values
print(a1, a2, a3)

*a1, a2, a3 = values
print(a1, a2, a3)



