a = [1]
f = []
b = 0

for n in range(2, 100000):
    a.append(a[len(a) - 1] + n)

while len(f) <= 500:
    for n in a:
        f = []
        for b in range(2, n + 1):
            if n % b == 0:
                b = n
                f.append(b)
                f.append(b)
        print(n, len(f), "diviseurs.")

print(b)