second = int(input("Input seconds: "))

hours = second // 3600
minutes = (second%3600) // 60
second = second - ((hours * 3600) + (minutes * 60))

print(f"{hours} Hours {minutes} Minutes {second} Second")