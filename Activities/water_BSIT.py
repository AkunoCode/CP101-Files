passage = input("Input passage: ").split(";")

if "1" in passage[0] and len(passage) > 1:
    position = passage[0].index("1")

    for row in range(1,len(passage)):
        check = []
        for index, column in enumerate(passage[row].split(",")):
            if index in [position, position+1, position-1]:
                if column == "1":
                    position = index
                    check.append(True)
                else:
                    check.append(False)
        else:
            if True not in check:
                print("No")
                break
    else:
        print("Yes")
                
elif len(passage) == 1 and "1" in passage[0]:
    print("Yes")
else:
    print("No")


