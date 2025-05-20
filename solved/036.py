# Completed on Tue, 20 May 2025, 22:41

def is_palindrome(string):
    result = True
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            result = False
            break
    return result

sum = 0

for n in range(1, 1000000):
    # The [2:] is to remove the "0b" prefix.
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
        sum += n

print(sum)