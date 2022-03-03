import os    # also imports os.path
import sys
# from module import class
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)

print("file_path: {}".format(file_path))

if not os.path.exists(file_path):
    print("NO such file:", file_path)
    sys.exit(1)

file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))

base_name = os.path.basename(file_path)
print("base_name: {}".format(base_name))
dir_name = os.path.dirname(file_path)
print("dir_name: {}".format(dir_name))
abs_path = os.path.abspath(file_path)
print("abs_path: {}".format(abs_path))

raw_file_ts = os.path.getmtime(file_path)
print("raw_file_ts: {}".format(raw_file_ts))  # Unix epoch time (seconds since 1-1-1970)
file_ts = datetime.fromtimestamp(raw_file_ts)
print("file_ts: {}".format(file_ts))

#   find foo -name '*.log' -print

start_dir = "."
for curr_dir, sub_dirs, files in os.walk(start_dir):
    try:
        sub_dirs.remove('.git')  # don't recurse into .git/
    except ValueError:
        pass
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:12d} {file_name}")
            # print("    {:12d} {}".format(file_size, file_name))
            # could write data to file, build dictionary

#   "{}".format(var)
#   f"{var}"



