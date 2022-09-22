"""
John Leo D. Echevaria (A22-34233)
CP101 - M002

"""
apple = int(input("How many apples are bought?: "))

dozen = apple // 12
piece = apple % 12
pay = (dozen * 100) + (piece * 10)

print(f"That is {dozen} dozens and {piece} pieces.")
print(f"The total amount is P{pay}")
