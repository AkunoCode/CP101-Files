given = int(input("\nPlease type a number to check its divisors: "))

x = [*range(1, (given+1))]
divisor = []
for i in range(0,len(x)):
    if given % x[i] == 0:
        divisor.append(x[i])
print(f"\nThe number {given} has {len(divisor)} divisors, which are: ")
for i in divisor:
    print(i, end=', ')