"""
FATHER AND SON

Hey, you! Let's make a family! Oh wait, sorry, that came out wrong, I meant through math. 
If I were to give you an array, I want you to be able to tell who the father and son is. 
The father is the largest sum possible, while the son is the smallest sum possible. 
Both are identified using only 3 elements from the array.

"""


input("Enter the size: ")

list = input("Enter the values: ").split()
list = [int(i) for i in list]
list.sort()

print(f"Father = {sum(list[-3:])}, Son = {sum(list[0:3])}")