for x in range(1,1001):
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    if sum == x:
        print(x,end=' ')

# for x in range(1,7):
#     print(f"\nX = {x}")
#     sum = 0
#     for i in range(1,x):
#         print(f"I = {i}")
#         if x % i == 0:
#             print(f"{i} is a divisor of {x}")
#             sum += i
#             print(f"Current divisor added to the previous = {sum}")
#         else:
#             print(f"{i} is NOT divisor of {x}")
#     if sum == x:
#         print(f"Sum of divisor equal to {x}")
#         print(f"{x} is a perfect number!")
#     else:
#         print(f"Sum of divisor NOT EQUAL to {x}")
#         print(f"{x} is NOT a perfect number!")