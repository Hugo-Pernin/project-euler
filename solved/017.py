# Completed on Mon, 19 May 2025, 18:33

def number_to_letters(number):
    result = ""
    string = str(n)
    if len(string) >= 4:
        result += "onethousand"
    if len(string) >= 3:
        hundred = int(string[len(string) - 3])
        tens = int(string[len(string) - 2])
        units = int(string[len(string) - 1])
        if hundred == 1:
            result += "one"
        elif hundred == 2:
            result += "two"
        elif hundred == 3:
            result += "three"
        elif hundred == 4:
            result += "four"
        elif hundred == 5:
            result += "five"
        elif hundred == 6:
            result += "six"
        elif hundred == 7:
            result += "seven"
        elif hundred == 8:
            result += "eight"
        elif hundred == 9:
            result += "nine"
        if hundred != 0:
            result += "hundred"
            if tens != 0 or units != 0:
                result += "and"
    if len(string) >= 2:
        tens = int(string[len(string) - 2])
        units = int(string[len(string) - 1])
        if tens == 1:
            if units == 0:
                result += "ten"
            elif units == 1:
                result += "eleven"
            elif units == 2:
                result += "twelve"
            elif units == 3:
                result += "thirteen"
            elif units == 4:
                result += "fourteen"
            elif units == 5:
                result += "fifteen"
            elif units == 6:
                result += "sixteen"
            elif units == 7:
                result += "seventeen"
            elif units == 8:
                result += "eighteen"
            elif units == 9:
                result += "nineteen"
        else:
            if tens == 2:
                result += "twenty"
            elif tens == 3:
                result += "thirty"
            elif tens == 4:
                result += "forty"
            elif tens == 5:
                result += "fifty"
            elif tens == 6:
                result += "sixty"
            elif tens == 7:
                result += "seventy"
            elif tens == 8:
                result += "eighty"
            elif tens == 9:
                result += "ninety"
            if units == 1:
                result += "one"
            elif units == 2:
                result += "two"
            elif units == 3:
                result += "three"
            elif units == 4:
                result += "four"
            elif units == 5:
                result += "five"
            elif units == 6:
                result += "six"
            elif units == 7:
                result += "seven"
            elif units == 8:
                result += "eight"
            elif units == 9:
                result += "nine"
    else:
        units = int(string[len(string) - 1])
        if units == 1:
            result += "one"
        elif units == 2:
            result += "two"
        elif units == 3:
            result += "three"
        elif units == 4:
            result += "four"
        elif units == 5:
            result += "five"
        elif units == 6:
            result += "six"
        elif units == 7:
            result += "seven"
        elif units == 8:
            result += "eight"
        elif units == 9:
            result += "nine"
    return result

sum = 0

for n in range(1, 1001):
    sum += len(number_to_letters(n))

print(sum)