# Completed on Fri, 4 Sep 2020, 18:21

b = 0

for n in range(1, 100000000000000000):
    for a in range(1, 21):
        if n % a == 0:
            b += 1
            if b == 20:
                print(n)
                exit()
        else:
            b = 0
            break