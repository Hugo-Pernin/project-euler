# Completed on Mon, 19 May 2025, 19:23

import itertools

string = "0123456789"
permutations = [''.join(p) for p in itertools.permutations(string)]

print(permutations[999999])