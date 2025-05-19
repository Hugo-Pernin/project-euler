sum = 0
divisors = 0

def d(a):
    global divisors
    divisors = 0
    for n in range(2, a):
        if a % n == 0:
            divisors += n

for c in range(1, 1001):
    if  d(divisors) == c and d(divisors) == c and c != divisors and c != divisors:
        sum += c + divisors

print(sum)