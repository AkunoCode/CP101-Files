students = {
    "Juan Dela Cruz":[90,85,87],
    "Rose Evangelista":[97,98,87],
    "Limuel Mendoza":[92,98,87]
    }

for x, y in students.items():
    print(f"Student: {x}")
    high = max(y)
    low = min(y)
    print(f"The highest quiz is quiz {y.index(high)+1} with grade of {high}")
    print(f"The lowest quiz is quiz {y.index(low)+1} with grade of {low}")

    print(f"Average grade is {((sum(y))/len(y)):.2f}")
    print()