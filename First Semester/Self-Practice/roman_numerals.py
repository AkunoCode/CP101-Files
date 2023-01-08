roman = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

num = input("Enter Roman Numeral: ").upper()
sum = 0
n = len(num)
i = 0

while i < n :
    if (i != n - 1 and roman[num[i]] < roman[num[i + 1]]):
        sum += roman[num[i + 1]] - roman[num[i]]
        i += 2
    else:
        sum += roman[num[i]]
        i += 1
print(sum)