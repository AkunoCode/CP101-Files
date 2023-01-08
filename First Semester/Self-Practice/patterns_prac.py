print()

for i in range(1,8):
    if i > 4 and i < 7:
        for j in range(1,6):
            if j == 1 or j == 5:
                print("*",end="")
            else:
                print(" ",end="")
        print()    
    elif i == 7: 
        for j in range(1,6):
            print("*",end="")
        print()
    else:
        for j in range(1,6):
            if j == 5:
                print("*",end="")
            else:
                print(" ",end="")
        print()

print()

for i in range(1,8):
    if i == 7:
        for i in range(1,6):
            print("*",end="")
        print()
    else:
        print("*",end="")
    print()

for i in range(1,8):
    if i == 1 or i == 4 or i == 7:
        for j in range(1,6):
            print("*",end="")
        print()
    else:
        print("*")
print()

for r in range(1,6):
    if r == 1:
        for c in range(1,6):
            if c == 3:
                print(" ", end="")
            else:
                print("*", end="")
    elif r == 2 or r == 3:
        for c in range(1,6):
            print("*",end="")
    elif r == 4:
        for c in range(1,6):
            if c >= 2 and c <= 4:
                print("*", end="")
            else:
                print(" ", end="")
    elif r == 5:
        for c in range(1,6):
            if c == 3:
                print("*", end="")
            else:
                print(" ", end="")
    print()
print()

c = 5

for i in range(c):
    for j in range(i, c):
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(c, -1, -1):
    for j in range(i, c):
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    print()

print()

for i in range(c):
    for j in range(i,c):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in reversed(range(c+1)):
    for j in range(i,c):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()