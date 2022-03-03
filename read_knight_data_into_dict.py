from pprint import pprint

def main():
    d = read_data()
    pretty_print(d)
    print_titles(d)
    print(get_field(d, 'Robin', 3))
    print(get_field(d, 'Arthur', 0))


def read_data():
    knight_data = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data.setdefault(name, (title, color, quest, comment))
            # knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print(data):
    pprint(data)

def print_titles(knight_data):
    for knight, data in knight_data.items():
        print(data[0], knight, data[2])

def get_field(data, knight, field):
    return data[knight][field]

if __name__ == '__main__':
    main()
