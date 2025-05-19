list = []

for d in range(1, 1000):
    if len(str(1/d)) > 10:
        for n in range(1, 10):
            if str(1/d)[len(str(1/d))-1] == str(1/d)[len(str(1/d))-n]:
                list.append(n)

list.sort()
print(list)