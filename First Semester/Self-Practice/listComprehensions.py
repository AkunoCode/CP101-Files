# num1 = []
# for i in range(1,101):
#     if "6" in str(i):
#         num1.append(i)

# print(num1)


# num2 = [i for i in range(1,101) if "6" in str(i)]
# print(num2)

# string = "Practice Problems to Drill List Comprehension in Your Head."
# string2 = (i for i in string if i not in "AEIOUaeiou")
# string3 = (i for i in string.split() if len(i) < 5)
# string4 = {i:len(i) for i in string.split(" ")}

# print(string)
# print(*string2)
# print(*string3)
# print(string4)

nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

print([i for i in nums if i % 8 == 0])
print([i for i in nums if "6" in str(i)])
print(len([i for i in string if i == " "]))
print("".join([char for char in string if char.lower() not in ["a","e","i","o","u"]]))
