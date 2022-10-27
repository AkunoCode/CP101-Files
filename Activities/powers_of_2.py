num = int(input("Enter the size: "))
elements = input("Enter the elements: ").split()

elements = [int(i) for i in elements]

powers = [i for i in elements if i in [2**n for n in range(10001)]]
powers.reverse()

if len(powers) == 0:
    print("none")
else:
    print("Powers of 2 =",*powers)