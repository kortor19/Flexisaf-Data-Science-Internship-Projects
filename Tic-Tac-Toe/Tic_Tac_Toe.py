#Tic-Tac-Toe
#Create a function to display the board in a user-friendly way.

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3 : (i+1)*3]))
        if i < 2:
            print("---------")
        print("\n")


#checking if player has won
#Winning combinations are rows, columns, and diagonals
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  #rows
        [0,3,6], [1,4,7], [2,5,7], #columns
        [0,4,8], [2,4,8] #diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

#check if the game is tie
#if no empty space remain, and no winner -> tie

def check_tie(board):
    return ' ' not in (board)

#AI Move (Simple Learning Agent)

import random

def ai_move(board):
    available = [i for i in range(9) if board[i] == ' ']
    return random.choice(available)

#Main Game loop
#Alternate turns between Human and AI
#After each move, check for win or tie.

def play_game():
    board = [' '] * 9
    current_player = "X" #humans start

    while True:
        print_board(board)

        if current_player == "X":
            move = int(input("Enter your move (0 - 8): "))
            if board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        else:
            print("AI is making a move...")
            move = ai_move(board)
        
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie")
            break
        #swich player
        current_player = "O" if current_player == "X" else "X"

#call main function
if __name__ == "__main__":
    play_game()
