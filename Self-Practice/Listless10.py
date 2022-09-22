a = []

while True:
    a.append(int(input("Please type a number: ")))
    if len(a) == 10:
        break

compare = int(input("Type a number to compare to: "))
lessorequal = []
for i in range(0,10):
    if a[i] <= compare:
        lessorequal.append(str(a[i]))
print(f"Here are the list of items less than or equal to {compare}.")

print(*lessorequal, sep=', ') # * symbol unpacks the list and seperator.
    