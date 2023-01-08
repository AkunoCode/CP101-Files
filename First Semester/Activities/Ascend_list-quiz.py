"""
ASCEND (CODECHUM LIST QUIZ)

Hey I've got this cool idea for an app! It's kind of simple but just hear me out. All the user has to do is enter a bunch of integers. 
Then the application prints the largest sum of a strictly ascending sequence of the array. 
A strictly ascending sequence is a sequence where the current number is always lesser than the next number. 
For example, the user enters 2 4 5 1 7 3, the output should be 11 (2 + 4 + 5).
Then that's it! I think this is going to be a hit! Don't you think? Well I do. If you help me then we're going to be rich!

Note: For this problem, a sequence must contain at least 2 numbers. If there is no sequence found, then the largest sum is 0.
"""

num_list = []
for i in range(1, 1+(int(input("Enter the size: ")))):
    num_list.append(int(input(f"Enter the element{i}: ")))

previous = 0
ascend = []
sums = []

for i in num_list:

    # If i is bigger than previous number it'll go into ascending list.
    if i > previous:
        ascend.append(i)
        previous = ascend[-1]
 
    # Else it'll get the sum of the current ascending list and append to sums list.
    # Then the ascend list will be cleared and the previous will turn into the current i.
    # Then the loop will continue and check again if the numbers are ascending.
    else:
        sums.append(sum(ascend))
        ascend.clear()
        ascend.append(i)
        previous = i

# After the loop has finished it'll take the sum of ascending list again and append it to sums.
# This is done just in case it'll have a continous ascending numbers. To make sure that we can get the sum.
else:
    sums.append(sum(ascend))


# Now if the biggest number in the sums list is equivalent to any number in the number list,
# then it means that there was no ascending numbers at all.
if max(sums) in num_list:
    print(f"Largest sum = 0")

# Else if the biggest number in the sums list is a different number then we can print it.
else:
    print(f"Largest sum = {max(sums)}")

