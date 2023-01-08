n = int(input("Enter the length of the butterfly: "))
upper_length = 4
lower_length = 3

for row1 in range(1, upper_length+1):
    for col1 in range(row1):
        print("*",end="")
    for space1 in range(row1,(int(n/2)+1)):
        print(" ", end="")
    for space2 in range(row1+1, (int(n/2)+1)):
        print(" ", end="")
    for col2 in range(row1):
        if row1 == upper_length and col2 == 0:
            print("", end = '')
        else:
            print("*", end="")
    print()

for row2 in range(1, lower_length+1):
    for col1 in range(row2, lower_length+1):
        print("*", end="")
    for space1 in range(1, row2):
        print(" ", end="")
    for space2 in range(row2):
        print(" ", end="")
    for col2 in range(row2, lower_length+1):
        print("*", end="")
    print()