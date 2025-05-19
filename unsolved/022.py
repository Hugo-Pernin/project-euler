with open("0022_names.txt") as file:
    list = set(map(str, file))

list = ''.join(sorted(list))

print(list)