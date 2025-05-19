list = [123456789]

for n in range(123456789, 9876543211):
    if n % 100000000 == 0:
        print(n)
    if "1" in str(n):
        if "2" in str(n):
            if "3" in str(n):
                if "4" in str(n):
                    if "5" in str(n):
                        if "6" in str(n):
                            if "7" in str(n):
                                if "8" in str(n):
                                    if "9" in str(n):
                                        if "0" in str(n) or n < 1000000000:
                                            list.append(n)
                                            if len(list) == 1000000:
                                                break

print(list[999999])