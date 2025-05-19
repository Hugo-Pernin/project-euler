# Completed on Mon, 19 May 2025, 21:51

"""
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

The top-right diagonal values are the squares of odd numbers: 9 = 3², 25 = 5², 49 = 7²...
The bottom-right diagonal values are rectangles of integers plus one: 3 = 1*2+1, 13 = 3*4+1, 31 = 5*6+1...
The bottom-left diagonal values are the squares of even numbers plus one: 5 = 2²+1, 17 = 4²+1, 37 = 6²+1...
The top-left diagonal values are rectangles of integers plus one: 7 = 2*3+1, 21 = 4*5+1, 43 = 6*7+1
So here is the solution:
"""

def solution(n):
    sum = 1 # center
    # top-right diagonal
    for i in range(3, n+1, 2):
        sum += i*i
    # bottom-right diagonal
    for i in range(1, n, 2):
        sum += i*(i+1)+1
    # bottom-left diagonal
    for i in range(2, n+1, 2):
        sum += i*i+1
    # top-left diagonal
    for i in range(2, n, 2):
        sum += i*(i+1)+1
    return sum

print(solution(1001))