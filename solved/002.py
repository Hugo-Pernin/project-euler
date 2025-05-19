# Completed on Fri, 4 Sep 2020, 18:02

f = [1, 2]
sum = 2

while f[len(f) - 1] < 4000000:
    f.append(f[len(f) - 1] + f[len(f) - 2])
    if f[len(f) - 1] % 2 == 0:
        sum += f[len(f) - 1]

print(sum)