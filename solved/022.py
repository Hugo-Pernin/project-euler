# Completed on Mon, 19 May 2025, 18:51

with open("../data/0022_names.txt") as file:
    names = file.read().split(",")

names.sort()

sum = 0

for i in range(len(names)):
    names[i] = names[i][1:-1] # Remove quotes
    local_sum = 0
    for j in range(0, len(names[i])):
        local_sum += ord(names[i][j]) - 64
    sum += local_sum * (i+1)

print(sum)