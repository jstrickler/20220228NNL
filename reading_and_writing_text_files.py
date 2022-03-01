import csv

file_path = 'DATA/mary.txt'

mary_in = open(file_path)   #  open(file_path, mode="r")
# read file here
mary_in.close()

with open(file_path) as mary_in:
    pass
# mary_in.close()

# read file line-by-line
with open(file_path) as mary_in:
    print(mary_in)
    for raw_line in mary_in:  #  mary_in.readline()
        word = raw_line.rstrip() # remove \n etc
        print(word)
print('-' * 60)

# read entire file into one string
with open(file_path) as mary_in:
    contents = mary_in.read()  # read entire file into one str obj
    print("raw:")
    print(repr(contents), '\n')
    print("normal:")
    print(contents)   #  output  str(contents) + '\n'
print('-' * 60)

# read entire file into list of lines WITH \n
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read entire file into list of lines WITHOUT \n
with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]  # or use generator expression
    print(all_lines_without_nl)

letter = 'x'
count = 0
output_filename = f"{letter}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(output_filename, "w") as words_out:
        with open("other_file.txt", "w") as other_out:
            for word in words_in:
                if word.startswith(letter):
                    count += 1
                    words_out.write(word)  # no \n needed -- already on 'word'
print(f"{count} words start with '{letter}'")

# "r"  read  (default)
# "w"  writing (deletes previous data if any)
# "a"  append (like "w", but doesn't delete previous data)
# "x"  writing (only opens if file does NOT exist)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

with open('DATA/FremontBridge.csv') as freemont_in:
    rdr = csv.reader(freemont_in)
    for row_index, row in enumerate(rdr):
        print(row)
        if row_index == 100:
            break


with open('DATA/alice.txt') as alice_in:
    total = 0
    for line in alice_in:
        total += line.count('Alice')
print(f"{total} occurrences of 'Alice'")