"""
Check if the inputted number is greater than 3 and print each that is greater than 3.
If none print none.

"""

num = input("Enter number: ")

none = True
for i in num:
    if int(i) > 3:
        print(i)
        none = False

if none:
    print("none")

print()