number = int(input("Enter the jeepney's number: "))
letter = input("Enter the jeepney's letter: ")

if number == 12:
    if letter.upper() == "A":
        location = "Carbon"
    elif letter.upper() == "C":
        location = "Panganiban"
    elif letter.upper() == "F":
        location = "Taboan"
    elif letter.upper() == "G" or letter.upper() == "I":
        location = "Mabolo"
    elif letter.upper() == "L":
        location = "Labangon"
elif number == 13:
    location = "Talamban"
else:
    location = "Capitol"

print(f"Usual location = {location}")