#Rock–Paper–Scissors program

#import the random library
import random

# Step 1: Define the possible choices in a list
choices = ["rock", "paper", "scissors"]

# Step 2: Get the user's choice using input prompt
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    # Step 3: Generate a random choice for the computer
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Step 4: Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!. draw game")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!. Take a cofee")
    else:
        print("Computer wins!. chill and try next time")
