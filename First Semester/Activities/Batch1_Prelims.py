km = float(input("How much did the taxi travel in km?: "))

full = (km // 10) * 100
extra = (km % 10) * 20

print(f"The fare will be P{full} plus {extra}")

print(f"The total amount is P{full + extra}")

