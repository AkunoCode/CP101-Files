"""
Fizzbuzz game: 

Count until a certain number.
If a number is divisible by 3 you say fizz.
If a number is divisible by 5 you say buzz.
If a number is divisible by both 3 and 5 you say fizzbuzz.
Else, just say the actual number.

"""

for i in range(1, int(input("What will be the max number?: ")) + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz",end=', ')
    elif i % 3 == 0:
        print("fizz", end=', ')
    elif i % 5 == 0:
        print("buzz", end=', ')
    else:
        print(i, end=', ')