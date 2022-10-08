"""
I've always had a hard time reading numbers. However, if they were in translated into words, I would have no problem reading them! If you could help me translate numbers to words then I would be very grateful.
If the number is composed of two words (e.g. 42), add a dash in between the two words (e.g. forty-two).

Spelling Guide:
20 - twenty
30 - thirty
40 - forty
50 - fifty
60 - sixty
70 - seventy
80 - eighty
90 - ninety

"""


number = int(input("Enter the number to be translated: "))

trans1 = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
}

trans2 = {
    20:"twenty",
    30:"thirty",
    40:"forty",
    50: "fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}
    
if number <= 20:
    print(f"{trans1[number]}")

elif number % 10 == 0:
    print(f"{trans2[number]}")
    
else:
    test1 = (number // 10) * 10 
    test2 = number % 10
    print(f"{trans2[test1]}-{trans1[test2]}")