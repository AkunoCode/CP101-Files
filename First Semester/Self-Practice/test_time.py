second = int(input("Enter the number of seconds: "))

hours = second // 3600
minutes = (second%3600) // 60
second = second - ((hours * 3600) + (minutes * 60))
if hours == 0:
    hours = "00"
elif hours % 10 != 0:
    hours = f"0{hours}"
if minutes == 0:
    minutes = "00"
elif minutes % 10 != 0:
    minutes = f"0{minutes}"
if second == 0:
    second = "00"
elif second % 10 != 0:
    second = f"0{second}"
print(f"Total time in the new format = {hours}:{minutes}:{second}")