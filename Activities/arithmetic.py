nth = int(input("Enter the number of terms: "))
d = int(input("Enter the value of the common difference: "))
start = int(input("Starting number: "))

a_sum = 0
for i in range(1, nth+1):
    arithmetic = start + (i - 1) * d
    a_sum += arithmetic
    
    print(arithmetic,end=" ")

print("\nThe sum of the arithmetic sequence is: ", a_sum)