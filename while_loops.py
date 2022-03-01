
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    file_name = input("Please enter file name (or q to quit): ")
    if file_name == 'q':
        break
    if len(file_name) == 0:
        print("Please enter a file name")
        continue
    print("Processing", file_name)

