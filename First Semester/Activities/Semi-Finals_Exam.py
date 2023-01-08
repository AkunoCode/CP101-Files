list = []
for i in range(1, 1+(int(input("Enter the size: ")))):
    list.append(int(input(f"Element #{i}: ")))

even = []
odd = []
for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

count = 1
list = even + odd
print("\nArranged numbers: ")
for i in list:
    print(f"Element #{count}: {i}")
    count += 1                          