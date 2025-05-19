# Completed on Fri, 4 Sep 2020, 18:07

with open("../data/primes_numbers.txt") as file:
    primes = set(map(int, file))
f = []

for n in primes:
    if 600851475143 % n == 0:
        f.append(n)

print(f[len(f)-1])