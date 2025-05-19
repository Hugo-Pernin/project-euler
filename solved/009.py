# Completed on Fri, 4 Sep 2020, 18:57

n = []

for d in range(1, 1000):
    n.append(d)

for a in range(1, 1000):
    for b in range(1, a + 1):
        if (a**2 + b**2)**0.5 in n:
            if a + b + (a**2 + b**2)**0.5 == 1000:
                print(a * b * (a**2 + b**2)**0.5)
                exit()