num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

# Approach is to check first for the smallest number.
# After that is the middle number.
# And automatically the remaining is the biggest number.

if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle, biggest = num2, num3
    elif num3 <= num2:
        middle, biggest = num3, num2

elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle, biggest = num1, num3
    elif num3 <= num1:
        middle, biggest = num3, num1

elif num3 <= num1 and num3 <= num2:
    smallest = num3
    if num2 <= num1:
        middle, biggest = num2, num1
    elif num1 <= num2:
        middle, biggest = num1, num2

print(f"{smallest} {middle} {biggest}")

# numbers = []
# numbers.append(num1)
# numbers.append(num2)
# numbers.append(num3)

# numbers.sort()
# for i in numbers:
#     print(i, end=" ")
