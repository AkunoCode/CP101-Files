"""

Coding challenge from LinkedIn Learning Course:
Algorithmic Thinking with Python: Foundations

There are 100 Doors in a row that are all initially closed.
You make a 100 passes by the doors and in each pass you toggle its state.
On the first pass you toggle each door, on second you toggle every second door (2, 4, 6)
And so on until you only visit the 100th Door.

"""

door = [False] * 101

# This is a nested for loop
for i in range(1, 101): # "You make 100 passes by the doors"
    for j in range (i, 101, i): # Defines where you start and how many skips each.
        door[j] = not door[j] # In each pass you toggle the state of the door

# Checks which door is open after the program.
for i in range(1, 101):
    if door[i] is True:
        print(i, end=', ')