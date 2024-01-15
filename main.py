import os
import random

demo_board = [0,1,2,3,4,5,6,7,8,9]
game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
spots_taken = []

# Draws the board to the terminal.
def draw_board(board):
    print(board[1] , "|" ,  board[2] , "|" , board[3])
    print("__|___|__")
    print(board[4] , "|" ,  board[5] , "|" , board[6])
    print("__|___|__")
    print(board[7] , "|" ,  board[8] , "|" , board[9])
    print("  |   |   ")

# Checks if anyone has won
def check_win(board):
    global Game

    # check each possible win each time

    if board[1] == board[2] == board[3] == 'X' or board[4] == board[5] == board[6] == 'X' or board[7] == board[8] == board[9] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X'  or board[3] == board[6] == board[9] == 'X' or board[1] == board[5] == board[9] == 'X'  or board[7] == board[3] == board[5] == 'X':
        print("You Win!!!")
        return True

    if board[1] == board[2] == board[3] == 'O' or board[4] == board[5] == board[6] == 'O' or board[7] == board[8] == board[9] == 'O' or board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O'  or board[3] == board[6] == board[9] == 'O' or board[1] == board[5] == board[9] == 'O'  or board[7] == board[3] == board[5] == 'O':
        print("Computer Wins :(!")
        return True

    else:
        return False

# Gets the players position, and plays it if it's a valid position.
def player_turn():
    draw_board(game_board)

    if not check_win(game_board):
        play = int(input("Enter the position you want to play: "))

        if play not in spots_taken:
            game_board[play] = "X"
            spots_taken.append(play)

        else:
            print("Whoops! Spot taken")
            player_turn()

        computer_turn()

    else:
        play_again()

# The computer plays by generating a random int as the position.
def computer_turn():
    if not check_win(game_board):

        pos = random.randint(1,9)
        print(pos)

        if pos not in spots_taken:
            game_board[pos] = "O"
            player_turn()

        else:
            computer_turn()

    else:
        play_again()

# replay functionality
def play_again():
    global game_board
    yes_no = input("Would you like to play again? (y/n)").lower()
    if yes_no == 'y':
        game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play()
    else:
        print("Thank you for playing!")

# Main game function
def play():
    print("Hello! Welcome to TIC TAC TOE!\nChoose a position in the grid below to play your X, and the computer will play against you")
    draw_board(demo_board)
    print("Enjoy!")

    player_turn()






play()

