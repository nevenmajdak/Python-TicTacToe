from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(l1)
    for i in range(3):
        print(l2)
        print(l31,game[i][0],l32,game[i][1],l32,game[i][2],l33)
        print(l2)
        print(l1)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        player = int(input("Enter your move: "))
        if (player < 1) or (player > 9):
            print('Enter number between 1 and 9')
            continue
        player -= 1
        x = player//3
        y = player%3
        field = board[x][y]
        #print(field, type(field))
        if type(field) is not int:
            print('Field already used.')
            continue
        board[x][y] = 'O'
        display_board(board)
        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free.append((i,j))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Horizontal
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign: return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign: return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign: return True
    # Vertical
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign: return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign: return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign: return True
    # Diagonal
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: return True
    # No Win scenario
    return False

def draw_comp_move(board):
    # The function draws the computer's move and updates the board.
    empty = make_list_of_free_fields(board)
    field = empty[randrange(len(empty))]
    
    board[field[0]][field[1]] = 'X'
    display_board(board)
    #print(field,field[0],field[1], type(field), type(field[1]))


game = [[1,2,3],[4,'X',6],[7,8,9]]
l1  = '+-------+-------+-------+'
l2  = '|       |       |       |'
l31 = '|  '
l32 = '  |  '
l33 = '  |'

win = False
display_board(game)

for i in range(4):
    enter_move(game)
    win = victory_for(game, 'O')
    if win is True:
        print('You Won!')
        break
    draw_comp_move(game)
    win = victory_for(game, 'X')
    if win is True:
        print('Comp Won!')
        break
if win is False:
    #display_board(game)
    print('Draw!')

# win = victory_for(game, 'X')
# if win is True: print('Win')
# if win is False: print('Draw')

