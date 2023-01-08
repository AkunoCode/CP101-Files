"""
Lawn Fence activity from IT class.

"""


lawn = int(input("Lawn: "))
fence = int(input("Fence: "))

flag = False

if lawn >= fence:
    for i in reversed(range(1,lawn+1)):
        if i == fence:
            flag = True
        if flag:
            print("**xx",end="")
        else:
            print("**",end="")
        print()
else:
    for i in reversed(range(1,fence+1)):
        if i == lawn:
            flag = True
        if flag:
            print("**xx",end="")
        else:
            print("  xx",end="")
        print()