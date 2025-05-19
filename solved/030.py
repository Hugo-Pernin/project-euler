# Completed on Sat, 19 Dec 2020, 12:22

res = 0

for n in range(2, 1000000):
    sum = 0
    a = len(str(n))-1
    while a != -1:
        sum += int(str(n)[a])**5
        a -= 1
    if sum == n:
        res += n

print(res)