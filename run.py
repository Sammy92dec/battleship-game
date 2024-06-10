import random


# Get inputs like row and column, Input to exit the game


def get_shot(guesses):
    while True:
        row = input("Please enter the row (0 - 6): ")
        if row.lower() == "exit":
            return "exit"

        try:
            row = int(row)
            col = int(input("Please enter the column (0 - 6): "))

            shot = 7 * row + col

            if shot < 0 or shot > 48:
                print("Incorrect coordinates, Please try again")
            elif shot in guesses:
                print("Incorrect, it's been used already")
            else:
                return shot
        except ValueError:
            print("Incorrect entry,Please enter your number.")
guesses = hit + miss

# Invalid name


def is_valid_name(name):
    return name.isalpha()

# Welcome text and Name Input


print("~~~~ Welcome to the Battleship!! ~~~~")
player_name = input("Enter your name: ")
while not is_valid_name(player_name):
    print("Invalid name.Please enter only alphabetic character.")
    player_name = input("Enter your name: ")
print("\n")
print(f"READY {player_name}! Your enemy's Battleboard is ready.")
print("\n")


# Instructions on how to play the game


print("You have a total of 20 turns to sink 3 hidden ships.")
print("Guess a row and a column (0 - 9).")
print("You will see X when you hit a ship,Otherwise O if you miss.")
print("Type'exit' instead of row number if you want to quit")
print("Choose Wisely,GOODLUCK!")
print("\n")


# Battle board 


def show_board(hit, miss):
    print("======= BATTLESHIP Board =======")
    print("    0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            if place in hit:
                ch = " X "
            elif place in miss:
                ch = " O "
            else:         
                ch = " * "
            row += ch
            place += 1
        print(x, "", row)
show_board()

def play_battleship_game():
    hit = []
    miss = []
    ships_found = 0
play_battleship_game()