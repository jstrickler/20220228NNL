import lxml.etree as et

root_tag = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        k = et.SubElement(root_tag, 'knight', title=title)
        name_tag = et.SubElement(k, 'name')
        name_tag.text = name
        et.SubElement(k, 'color').text = color
        et.SubElement(k, 'quest').text = quest
        et.SubElement(k, 'comment').text = comment

doc = et.ElementTree(root_tag)
doc.write("knights.xml", pretty_print=True, xml_declaration=True)


xml_doc = et.tostring(root_tag, pretty_print=True, xml_declaration=True).decode()
print(xml_doc)

