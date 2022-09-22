"""

You are given a string .
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

"""

from itertools import combinations

s, k = input().split()

for i in range(1,(int(k)+1)):
    list_combination = list(combinations(s,int(i)))

    for item in range(0,len(list_combination)):
        list_combination[item] = sorted(list_combination[item])

    list_combination.sort()

    for item in list_combination:
        print(*item, sep='')