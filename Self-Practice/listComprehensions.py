num1 = []
for i in range(1,101):
    if "6" in str(i):
        num1.append(i)

print(num1)


num2 = [i for i in range(1,101) if "6" in str(i)]
print(num2)

string = "Practice Problems to Drill List Comprehension in Your Head."
string2 = (i for i in string if i not in "AEIOUaeiou")
string3 = (i for i in string.split() if len(i) < 5)
string4 = {i:len(i) for i in string.split(" ")}

print(string)
print(*string2)
print(*string3)
print(string4)
