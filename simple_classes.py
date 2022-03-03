from zipfile import ZipFile


cities = list()
cities.append('Durham')
cities.append('Albany')
cities.append('West Mifflin')
print(cities)   # print(str(list))
print(type(list), type(cities))

z = ZipFile('spam.zip', mode="w")
print(type(z), type(ZipFile))
z.write('pastable.py')
z.close()

class Dog:
    def bark(self):
        print("woof! woof!")

d1 = Dog("Nellie", "english shepherd")
d2 = Dog("Andy", "mutt")
d3 = Dog("Little Bear", "english shepherd")

d1.bark()
d3.bark()








