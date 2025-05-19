# Completed on Sat, 5 Sep 2020, 13:08

maxstep = 0
solution = 0

for m in range(1, 1000001):
    step = 0
    n = m
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        step += 1
    if step > maxstep:
        maxstep = step
        solution = m

print(solution)