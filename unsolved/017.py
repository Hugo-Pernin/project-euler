sum = 39

for n in range(11, 1000):
    if len(str(n)) == 3:
        if int(str(n)[0]) == 1 or int(str(n)[0]) == 2 or int(str(n)[0]) == 6:
            sum += 13
        if int(str(n)[0]) == 4 or int(str(n)[0]) == 5 or int(str(n)[0]) == 9:
            sum += 14
        if int(str(n)[0]) == 3 or int(str(n)[0]) == 7 or int(str(n)[0]) == 8:
            sum += 15
        if int(str(n)[1]) == int(str(n)[2]) == 0:
            sum -= 3
        if int(str(n)[1]) == 1:
            if int(str(n)[2]) == 0:
                sum += 3
            if int(str(n)[2]) == 1 or int(str(n)[2]) == 2:
                sum += 6
            if int(str(n)[2]) == 5 or int(str(n)[2]) == 6:
                sum += 7
            if int(str(n)[2]) == 3 or int(str(n)[2]) == 4 or int(str(n)[2]) == 8 or int(str(n)[2]) == 9:
                sum += 8
            if int(str(n)[2]) == 7:
                sum += 9
        else:
            if int(str(n)[1]) == 4 or int(str(n)[1]) == 5 or int(str(n)[1]) == 6:
                sum += 5
            if int(str(n)[1]) == 2 or int(str(n)[1]) == 3 or int(str(n)[1]) == 8 or int(str(n)[1]) == 9:
                sum += 6
            if int(str(n)[1]) == 7:
                sum += 7
            if int(str(n)[2]) == 1 or int(str(n)[2]) == 2 or int(str(n)[2]) == 6:
                sum += 3
            if int(str(n)[2]) == 4 or int(str(n)[2]) == 5 or int(str(n)[2]) == 9:
                sum += 4
            if int(str(n)[2]) == 3 or int(str(n)[2]) == 7 or int(str(n)[2]) == 8:
                sum += 3
    else:
        if int(str(n)[0]) == 1:
            if int(str(n)[1]) == 1 or int(str(n)[1]) == 2:
                sum += 6
            if int(str(n)[1]) == 5 or int(str(n)[1]) == 6:
                sum += 7
            if int(str(n)[1]) == 3 or int(str(n)[1]) == 4 or int(str(n)[1]) == 8 or int(str(n)[1]) == 9:
                sum += 8
            if int(str(n)[1]) == 7:
                sum += 9
        else:
            if int(str(n)[0]) == 4 or int(str(n)[0]) == 5 or int(str(n)[0]) == 6:
                sum += 5
            if int(str(n)[0]) == 2 or int(str(n)[0]) == 3 or int(str(n)[0]) == 8 or int(str(n)[0]) == 9:
                sum += 6
            if int(str(n)[0]) == 7:
                sum += 7
            if int(str(n)[1]) == 1 or int(str(n)[1]) == 2 or int(str(n)[1]) == 6:
                sum += 3
            if int(str(n)[1]) == 4 or int(str(n)[1]) == 5 or int(str(n)[1]) == 9:
                sum += 4
            if int(str(n)[1]) == 3 or int(str(n)[1]) == 7 or int(str(n)[1]) == 8:
                sum += 3

print(sum + 11)