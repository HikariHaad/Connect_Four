import time, os, random

# global constants

ROWS = 6
COLS = 7
PLAYERS = 2
MARKERS = ["X", "O", "V", "H", "M"] # a list that we shift in for different player number


# the main printing function which displays the board and the winning statement if a player wins
def show(win = False):
    os.system("clear")

    for x in range(COLS):
        print('   ' + chr(x + 65), end='')

    print('\n +' + '---+' * COLS)

    for y in range(ROWS):
        print(' |', end='')
        for x in range(COLS):
            print(' ' + board[y][x], '|', end='')  # printing the board
        print('\n +' + '---+' * COLS)

    # checking for win from the main loop

    if win:
        print()
        print("CONGRATULATIONS PLAYER " + str(turn + 1) + " WINS.")


# this function inserts a symbol in the said col given that the chosen col is legitimate (checked in the main loop)
def insert(location):

    my_col = ord(location) - 65
    change = True

    while change:
        change = False

        for y in range(ROWS - 1, -1, -1):
            if board[y][my_col] == " ":
                board[y][my_col] = MARKERS[turn]
                break
            else:
                continue


# check if a col has empty space (if it does not, it is not a valid input)
def col_check(col):
    checklist = []
    for y in range(ROWS):
        checklist.append(board[y][col])
    return ' ' in checklist


# main win condition checking function
def win_check():
    # win_check for horizontal connected 4
    for y in range(ROWS):
        for x in range(COLS):
            try:
                if board[x][y] == MARKERS[turn] and board[x][y+1] == MARKERS[turn] and board[x][y+2] == MARKERS[turn] and board[x][y+3] == MARKERS[turn]:
                    return True
            except IndexError:
                continue

    # win_check for vertical connected 4
    for y in range(ROWS):
        for x in range(COLS):
            try:
                if board[y][x] == MARKERS[turn] and board[y+1][x] == MARKERS[turn] and board[y+2][x] == MARKERS[turn] and board[y+3][x] == MARKERS[turn]:
                    return True
            except IndexError:
                continue

    # win_check for diagonals connected 4

    for y in range(ROWS):
        for x in range(COLS):
            try:
                if board[y][x] == MARKERS[turn] and board[y+1][x+1] == MARKERS[turn] and board[y+2][x+2] == MARKERS[turn] and board[y+3][x+3] == MARKERS[turn]:
                    return True
            except IndexError:
                continue

    for y in range(ROWS):
        for x in range(COLS):
            try:
                if board[y][x] == MARKERS[turn] and board[y+1][x-1] == MARKERS[turn] and board[y+2][x-2] == MARKERS[turn] and board[y+3][x-3] == MARKERS[turn]:
                    return True
            except IndexError:
                continue

    return False


# checking the legitimate letters depending upon the dimensions
letters = []
for col_ in range(COLS):
    letters.append(chr(col_ + 65))

board = []
for rows in range(ROWS):
    row_list = []
    for cols in range(COLS):
        row_list.append(" ")
    board.append(row_list)

turn = random.randint(0, PLAYERS - 1)

game = True

# main loop for the program
while game:

    invalid = True
    show()
    # loop to check a valid input
    while invalid:
        input_ = input("PLAYER " + str(turn + 1) + ", please enter a column: ")
        if input_ in letters and col_check(ord(input_) - 65):
            invalid = False
        else:
            print("Please enter a valid uppercase empty column")

    # insert the symbol if the given input is valid in the board
    insert(input_)

    # print the updated board
    show()

    # check for the win if 4 connected symbols seen
    if win_check():
        show(True)
        game = False

    # change the turn
    turn = (turn + 1) % PLAYERS
