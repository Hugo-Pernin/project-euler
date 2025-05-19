# Completed on Fri, 4 Sep 2020, 18:32

f = [2, 3, 5, 7, 11]

for n in range(13, 100000000, 2):
    for o in range(3, round(n**0.5+1), 2):
        if n % o == 0:
            break
    else:
        f.append(n)
    if len(f) == 10001:
        print(f[10000])
        break