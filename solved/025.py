# Completed on Fri, 18 Dec 2020, 13:47

f = [0, 1]
for n in range(1, 10001):
    f.append(f[n]+f[n-1])
    if len(str(f[len(f)-1])) == 1000:
        print(len(f)-1)
        break