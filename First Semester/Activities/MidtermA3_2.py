"""
We need to start saving money people! I've noticed that we've been spending more money on electricity than everything else combined. In order for us to keep track of our electricity usage, we need to calculate our monthly cost based on our meter readings.

Cost:
0 to 100 kWh - P150.00
101 to 500 - P150.00 + 0.5 for each kWh over 100
over 500 - P350.00 + 0.3 for each kWh above 500

"""

reading = int(input("Enter the rate of consumption (kWh): "))

if reading >= 0 and reading <= 100:
    price = 150.00
elif reading <= 500:
    reading -= 100
    price = 150.00 + (reading* 0.5)
elif reading > 500:
    reading -= 500
    price = 350.00 + (reading* 0.3)

print(f"Total cost = P{price:.2f}")