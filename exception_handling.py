# A:
file_path = "DATA/wombats.txt"
try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except FileNotFoundError as err:
    print(err)
print("finished with wombats\n")

# B:
file_path = "DATA/breakfast.txt"
with open(file_path) as file_in:
    foods = [f.rstrip() for f in file_in]

try:
    print(foods[37])
except IndexError as err:
    print(err)

print("finished with foods\n")

# C:
nums = [3250, 0, 800, 80, 0.7, 1000, 0, 32, "123", 255, 0, 400, 5, 5000]
zero_count = 0
for n in nums:
    try:
        result = 10000 / n
    except ZeroDivisionError as err:
        print(err)
        zero_count += 1
    except (TypeError, ValueError) as err:
        print(err)
    else:  # no exceptions were raised
        print(result)

print("zero_count: {}".format(zero_count))


print("All done.")
