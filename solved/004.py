# Completed on Fri, 4 Sep 2020, 18:17

list = []

for n in range(100, 1000):
    for a in range(100, 1000):
        if str(a * n) == str(a * n)[::-1]:
            list.append(a * n)

list.sort()
print(list[len(list)-1])