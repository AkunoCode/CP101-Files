import random

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

rounds = int(input("\nHow many rounds would you like to play?: "))
match = 1
while match != rounds:
    player = input("\nRock, Paper, or Scissors?: ").lower()
    bot = random.choice(["rock","paper","scissors"])
    print(f"\n{player.title()} vs {bot.title()}")
    print(compare(player,bot))
    match += 1
    
