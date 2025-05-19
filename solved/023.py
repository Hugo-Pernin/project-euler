abundant = []
sum = 0

for n in range(1, 28124):
    b = 0
    for a in range(1, n):
        if n % a == 0:
            b += a
    if b > n:
        abundant.append(n)

print(abundant)

for n in range(1, 28124):
    #print(n)
    for c in abundant:
        if c > n:
            sum += int(n)
            break
        if n - c in abundant:
            break

print(sum)