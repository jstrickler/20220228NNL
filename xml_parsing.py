import lxml.etree as et

doc = et.parse('DATA/solar.xml')

root_element = doc.getroot()

print(doc)
print(root_element)
print(root_element.tag)

for element in root_element:
    print(element.tag)
    if element.tag.endswith('planets'):
        for planet in element.findall('planet'):
            print(f"    {planet.get('planetname')}")
            for moon in planet.findall('moon'):
                print(f"        {moon.text}")

print('-' * 60)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")




