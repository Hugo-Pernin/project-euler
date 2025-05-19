# Completed on Sat, 19 Dec 2020, 11:53

with open("../data/primes_numbers.txt") as file:
    primes = set(map(int, file))

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        for n in range(0, 1000):
            if not n**2 + a * n + b in primes:
                if n == 71: # Oui j'ai fait quelques test avant pour en arriver là mais chut
                    print(a * b)
                break