number = str(input("Enter the number: "))
count = -1
zero = 0

while True:
    if number[count] == "0":
        zero += 1
        count -= 1
    else:
        break

print(f"Trailing zeroes = {zero}")