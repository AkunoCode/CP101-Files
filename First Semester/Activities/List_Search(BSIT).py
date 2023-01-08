"""
Problem 1:

Create a program that will accept 5 integer number and store it in a list. Also, accept a search value.
Display how many times the search value exists in the list and the index number where it can be found.
If the search value does not exist in the list, display Not Found.
"""

num = []
for i in range(1,6):
    num.append(int(input(f"Enter No. {i}: ")))
search = int(input("Enter search value: "))

if search in num:
    num = [i for i,x in enumerate(num) if x == search]
    print(f"{search} can be found {len(num)} time(s) at index {num}")
else:
    print("Not Found")

"""
Problem 2:

Create a program that will accept a positive and negative integer number and store it in a list until the user enter /.
Display the sum and average of all input and the highest and lowest value index number where it can be found.
"""

inp = ""
count = 1
num = []
while inp != "/":
    inp = input(f"Enter No. {count}: ")
    count += 1
    if inp != "/":
        inp = int(inp)
        num.append(inp)
    else:
        pass
else:
    num_eval = num.copy()
    num_eval.sort()
    print(f"The sum of all inputs is {sum(num)}")
    print(f"The average of all inputs is {(sum(num)/len(num)):.2f}")
    print(f"The highest input is {num_eval[-1]} found at the index {num.index(num_eval[-1])}")
    print(f"The lowest input is {num_eval[0]} found at the index {num.index(num_eval[0])}")


"""
Problem 3:

Create a program that will accept a positive integer number and store it in a list until the user enters 0.
Display the list of all even and add number and the index numbers where they can be found.
"""

num = 1
count = 1
list_num = []
while num != 0:
    num = int(input(f"Enter No. {count}: "))
    if num != 0:
        list_num.append(num)
        count += 1
else:
    even = [(i,x) for i,x in enumerate(list_num) if x % 2 == 0]
    odd = [(i,x) for i,x in enumerate(list_num) if x % 2 != 0]
    print(f"List of even numbers: {[even[i][1] for i in range(len(even))]}")
    print(f"Even numbers can be found at the index: {[even[i][0] for i in range(len(even))]}")
    print(f"List of odd numbers: {[odd[i][1] for i in range(len(odd))]}")
    print(f"Odd numbers can be found at the index: {[odd[i][0] for i in range(len(odd))]}")

