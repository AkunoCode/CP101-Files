"""
Print numbers from 0 to input. 10 numbers per row.
Input must be less than 50.
"""


number = int(input("Enter size: "))

# Check if number is less than 50
if number < 50:
    # Count will be the counter
    count = 0
    while count < number:
        # 10 numbers per row
        for x in range(1,11): 
            print(count, end=" ")
            # Increment to count
            count += 1
            # So it won't exceed the number.
            if count == number:
                break
        print()
else:
    print("Number must be less than 50!")