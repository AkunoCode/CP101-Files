roman_num = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

print(tuple(**roman_num))


# num = input("Roman Numeral: ").upper()

# value = 0
# for i in range(len(num)):
#     if i > 0 and roman_num[num[i]] > roman_num[num[i-1]]:
#         value += roman_num[num[i]] - 2 * roman_num[num[i-1]]
#     else:
#         value += roman_num[num[i]]

# print(f"Roman numeral {num} is equal to {value}")


