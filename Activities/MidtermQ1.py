package = input("Enter the letter of package (A, B, C): ")
gallons = int(input("Enter the number of gallons consumed: "))

if package == "A":
    price = (gallons * 0.002) + 250
elif package == "B":
    # First 4-Mil gallons is P5,000, if it exceeds
    # every gallons above 4-Mil gallons is worth P0.002
    # (It's not "For every 4-Mil" so you shouldn't use % )
    if gallons >= 4_000_000:
        gallons -= 4_000_000
        price = (gallons * 0.002) + 5_000
    else:
        # Less than 4-Mil is auto P5000
        price = 5000.00
elif package == "C":
    # P8,000 if less than 4-Mil gallons
    if gallons <= 4_000_000:
        price = 8_000.00
    # P14,000 if more than 4-Mil but less than 10-Mil gallons 
    elif gallons <= 10_000_000:
        price = 14_000.00
    # Else, Greater than 10-Mil is P18,000
    else:
        price = 18_000

print(f"Total cost = P{price:.2f}")