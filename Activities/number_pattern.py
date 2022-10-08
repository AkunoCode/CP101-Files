number = int(input("Enter a number: "))

staph = False
limit = 1
start = 1

for num in range(1,number+1): # Outer Loop
    end = start + limit
    for i in range(start, end): # Inner Loop
        if i > number: # Limiter so it won't exceed the inputted number, to break out of inner loop.
            staph = True
            break
        else: # Print the column
            print(i, end="")
    if staph: # To break out of the outer loop.
        break
    else: # Incrementing and updating values.
        limit += 1
        start = end
        print()
    
        