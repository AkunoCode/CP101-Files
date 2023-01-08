# Taking input number and bit-position
x1 = (input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = (input("Enter y1: "))
y2 = int(input("Enter y2: "))
z1 = (input("Enter z1: "))
z2 = int(input("Enter z2: "))

# Converting to Binary
x1 = f'{int(x1):b}'
y1 = f'{int(y1):b}'
z1 = f'{int(z1):b}'

# Reversing
x1 = x1[::-1]
y1 = y1[::-1]
z1 = z1[::-1]

# Checking the Truthfulness of the Bits
truth = []
try:
    if x1[x2] == "0":
        truth.append(False)
    else:
        truth.append(True)
except IndexError:
    truth.append(False)

try:
    if y1[y2] == "0":
        truth.append(False)
    else:
        truth.append(True)
except IndexError:
    truth.append(False)
    
try:
    if z1[z2] == "0":
        truth.append(False)
    else:
        truth.append(True)
except IndexError:
    truth.append(False)


if (False in truth and True in truth) or (True in truth and False in truth):
    print(0)
elif False in truth and True not in truth:
    print(0)
else:
    print(1)