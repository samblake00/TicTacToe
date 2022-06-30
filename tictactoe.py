# ----- Global Variables -----

#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If game is still going
game_going = True

#Winner? Tie?
winner = None


#Whose turn is it?
current_player = "X"

#Display tic tac toe board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a game of tic tac toe
def play_game():
    # Display initial board
    display_board()

    #While the game is still going
    while game_going:
        #Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    #The game has end
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid position. Go again.")



    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #access global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no winner
        winner = None
    return

def check_rows():
    #set up global variables
    global game_going
    #check if any of the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_going = False
    #Return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    #set up global variables
    global game_going
    #check if any of the rows have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_going = False
    #Return the winner X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    #set up global variables
    global game_going
    #check if any of the rows have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_going = False
    #Return the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_going
    if "-" not in board:
        game_going = False
    return

def flip_player():
    # global variables
    global current_player
    #if the current player was x, then change to o
    if current_player == "X":
        current_player = "O"
    #if the current player was o, then change to x
    elif current_player == "O":
        current_player = "X"
    return

play_game()