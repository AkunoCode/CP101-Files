import random

print("\n\nThink of a number within 1 - 100 and the robot will guess")
print("\nType higher, lower, or correct if depending on the guess of the robot")

a = 1
b = 101
correct = False
no_guess = 1
guessed = []

while no_guess <= 10:
    robot_guess = random.randint(a,b)
    if robot_guess in guessed:
        continue
    else:
        guess = input(f"\n\tI'm guessing its {robot_guess}! Is it correct?: ")
        if guess.lower() == "higher":
            a = robot_guess
            no_guess += 1
            guessed.append(robot_guess)
        elif guess.lower() == "lower":
            b = robot_guess
            no_guess += 1
            guessed.append(robot_guess)
        elif guess.lower() == "correct":
            print("\nYey! Thank you for playing with me~\n")
            correct = True
            break
        else:
            print('\nPlease type "Higher","Lower", or "Correct" only :((')

if not correct:
    print("\nYou won! I ran out of guess :((")

