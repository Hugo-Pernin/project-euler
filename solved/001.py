# Completed on Fri, 4 Sep 2020, 17:49

n = 1
sum = 0

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

print(sum)