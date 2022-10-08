"""
Alternating number pattern problem from IT class.
x , 2x+1 ...

"""


num = int(input("Enter the number of elements: "))

sequence = []
for i in range(1, num+1):
    sequence.append(i)
    x = (2*i)+1
    sequence.append(x)

print(*sequence[:num])