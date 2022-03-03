import fileinput
from argparse import ArgumentParser, RawDescriptionHelpFormatter

description = """
faux grep

A small program that works like the unix Grep command. 

Syntax:

faux_grep.py word-to-find file ...

Does not support regular expressions (yet).

"""

parser = ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)

parser.add_argument('-i', dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument('-n', dest="show_name", action="store_true", help="display file name")
parser.add_argument('word', help="word to find")
parser.add_argument('files', nargs='+', help="files to search")

args = parser.parse_args()  # object with arguments

for raw_line in fileinput.input(args.files):
    if args.ignore_case:
        search_line = raw_line.lower()
    else:
        search_line = raw_line
    target = args.word.lower() if args.ignore_case else args.word

    if target in search_line:
        line = raw_line.rstrip()
        if args.show_name:
            print(fileinput.filename(), end=' ')
        print(line)

