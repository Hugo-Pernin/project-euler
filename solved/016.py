# Completed on Sat, 5 Sep 2020, 17:18

a = str(2**1000)
b = 0

for n in range(0, len(a)):
    b += int(a[n])

print(b)