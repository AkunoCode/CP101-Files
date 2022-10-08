""" 
Make a program that will take an input and count the number of words, letters,
numbers, and symbols contained in the input.

"""

scan = input("\nEnter something to scan: ")
letter = 0
number = 0
symbols = 0

for i in scan:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        number += 1
    elif i == " ":
        continue
    else:
        symbols += 1

words = len(scan.split())

print(f"""
Input:
\"{scan}\" 

Contains the following:
Words = {words}
Letters = {letter}
Numbers = {number}
Symbols = {symbols}
""")