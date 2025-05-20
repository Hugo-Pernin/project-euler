# Completed on Tue, 20 May 2025, 09:58

import math

def d(n):
    result = 1 # 1 divides everyone
    for divisor in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % divisor == 0:
            result += divisor + n // divisor
    return result

def is_amicable(n):
    return d(d(n)) == n and d(n) != n

sum = 0

for i in range(1, 10001):
    if is_amicable(i):
        sum += i

print(sum)