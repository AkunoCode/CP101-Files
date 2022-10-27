"""
1. Lost My Number:
Check if element is in a list.
"""
folder = []
for i in range(1,(int(input("Enter the size of the array: ")))+1):
    folder.append(int(input(f"Element #{i}: ")))

if (int(input("Enter the number of the folder: "))) in folder:
    print("YES")
else:
    print("NO")

"""
2. Some total:
Print the total of the list.
"""
cash = []
for i in range(int(input("Enter the number of cash: "))):
    cash.append(int(input()))

print("\nTotal:")
print(*cash, sep=" + ",end=" = ") ; print(f"{sum(cash)}")

"""
High Scorer 3:
Get the highest value out of the given dictionary
"""
students = {
    "Mark":80,
    "Mario": 98,
    "Richard": 78
}
print(max(students,key=students.get))

