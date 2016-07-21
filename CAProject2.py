#Code Academy project: simplistic game of battleships

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! Hundreds of men and women are dead at your hands, and thousands of innocents in some nameless foreign nation have had their loved ones callously taken from them! You will have nightmares about this day almost every night for the rest of your life.")
        post = input("Would you like to tell yourself you were only following orders? (y/n)")
        if(post == "y"):
            print("It changes nothing.")
        else:
            print("Good. Though it may be technically true, running from the magnitude of what you have done will make nobody happy. Thank you for playing.")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0     or guess_col > 4):
             print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            
    print(turn + 1)
    print_board(board)
    if(turn==3):
                print("Game Over! Your vessel has failed in its singular duty, and though you have kept your hands free of blood for another day, you have endangered the lives and careers of your men, and the ship you let escape will, in all likelihood, go on to kill hundreds of your countrymen - those to whom you swore a solemn oath to protect - , many of them will be civilians, some children, util some other, more competent Captain shoulders the burden that should by all rights have been yours, and puts an end to their rampage.")	