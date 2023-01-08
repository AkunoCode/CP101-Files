"""
Any year divisible by 4 is a leap year unless
    any year divisible by 100 is not a leap year unless
        any year divisible by 400 is a leap year

"""

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))