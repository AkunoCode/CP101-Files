end = int(input("Enter a number: "))
divisor = []
for x in range(1,end+1):
    for i in range(1,x+1):
        if x % i == 0:
            divisor.append(i)

    if len(divisor) == 2:
        if x in divisor and 1 in divisor:
            divisor.clear()
            continue
        else:
            print(x)
            divisor.clear()
    else:
        print(x)
        divisor.clear()