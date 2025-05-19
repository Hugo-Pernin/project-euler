# Completed on Sun, 6 Sep 2020, 11:26

from math import factorial

sum = 0

for n in str(factorial(100)):
    sum += int(n)

print(sum)