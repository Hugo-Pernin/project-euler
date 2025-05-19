# Completed on Fri, 4 Sep 2020, 19:01

sum = 0

for n in range(3, 2000001, 2):
    for o in range(3, round(n**0.5+1), 2):
        if n % o == 0:
            break
    else:
        sum += n

print(sum + 2)