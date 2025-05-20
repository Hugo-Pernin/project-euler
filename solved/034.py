# Completed on Tue, 20 May 2025, 22:29

# We only need 10 small factorials, so we can pre-calculate them
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# With 6 digits, the max sum is 6*(9!) = 2 177 280. This sum is superior to 999 999.
# With 7 digits, the max sum is 7*(9!) = 2 540 160. This sum is inferior to 9 999 999 so the limit has seven digits.
# That's why my upper bound is 10**7.
# The lower bound is 10 because as said in the problem, one-digit numbers aren't considered as sums.

result = 0

for n in range(10, 10000000):
    facts_sum = 0
    string = str(n)
    for i in range(len(string)):
        facts_sum += facts[int(string[i])]
    if facts_sum == n:
        result += n

print(result)