# Completed on Sat, 19 Dec 2020, 11:58

list = []

for a in range(2, 101):
    for b in range(2, 101):
        if not a**b in list:
            list.append(a**b)

print(len(list))