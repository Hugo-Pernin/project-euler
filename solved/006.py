# Completed on Fri, 4 Sep 2020, 18:26

a = 0
b = 0

for n in range(1, 101):
    a += n**2
    b += n

print(b**2 - a)