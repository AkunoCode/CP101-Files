# num = input("Enter number: ")

# none = True
# for i in num:
#     if int(i) > 3:
#         print(i)
#         none = False

# if none:
#     print("none")

# print()


num = input("Enter number: ")


while len(num) > 1:
    product = 1
    for i in num:
        i = int(i)
        product *= i
    num = str(product)
    print(f"The product is {product}")
    print(f"Enter the number: {num}")
else:
    print(f"The fictitious root is {num}")