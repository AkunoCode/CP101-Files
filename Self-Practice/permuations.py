from itertools import permutations

s, k = input("\nInput a string combination and an integer: ").split()

list_permuation = list(permutations(s,int(k)))
list_permuation.sort()

for item in list_permuation:
    print(item)