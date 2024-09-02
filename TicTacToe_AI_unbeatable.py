from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(l1)
    for i in range(3):
        print(l2)
        print(l31, board[i][0], l32, board[i][1], l32, board[i][2], l33)
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
        x = player // 3
        y = player % 3
        field = board[x][y]
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
                free.append((i, j))
    return free

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Horizontal
    for row in board:
        if row[0] == row[1] == row[2] == sign: return True
    # if board[0][0] == board[0][1] == board[0][2] == sign: return True
    #if board[1][0] == board[1][1] == board[1][2] == sign: return True
    #if board[2][0] == board[2][1] == board[2][2] == sign: return True
    # Vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign: return True
    #if board[0][0] == board[1][0] == board[2][0] == sign: return True
    #if board[0][1] == board[1][1] == board[2][1] == sign: return True
    #if board[0][2] == board[1][2] == board[2][2] == sign: return True
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] == sign: return True
    if board[0][2] == board[1][1] == board[2][0] == sign: return True
    # No Win scenario
    return False

def minimax(board, depth, is_maximizing):
    if victory_for(board, 'X'):
        return 1
    if victory_for(board, 'O'):
        return -1
    if not make_list_of_free_fields(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in make_list_of_free_fields(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, False)
            board[i][j] = i * 3 + j + 1
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in make_list_of_free_fields(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, True)
            board[i][j] = i * 3 + j + 1
            best_score = min(score, best_score)
        return best_score

def draw_comp_move(board):
    # The function draws the computer's move and updates the board using an enhanced strategy.
    def check_immediate_win_or_block(board, sign):
        for (i, j) in make_list_of_free_fields(board):
            board[i][j] = sign
            if victory_for(board, sign):
                board[i][j] = 'X'
                return True
            board[i][j] = i * 3 + j + 1
        return False
    
    # Check if AI can win in the next move
    if check_immediate_win_or_block(board, 'X'):
        display_board(board)
        return

    # Check if the player can win in the next move, and block them
    if check_immediate_win_or_block(board, 'O'):
        display_board(board)
        return

    # If no immediate win or block is needed, proceed with Minimax
    best_score = -float('inf')
    best_move = None
    for (i, j) in make_list_of_free_fields(board):
        board[i][j] = 'X'
        score = minimax(board, 0, False)
        board[i][j] = i * 3 + j + 1
        if score > best_score:
            best_score = score
            best_move = (i, j)
    board[best_move[0]][best_move[1]] = 'X'
    display_board(board)

game = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = '+-------+-------+-------+'
l2 = '|       |       |       |'
l31 = '|  '
l32 = '  |  '
l33 = '  |'

win = False
current_player = 'player' if randrange(2) == 0 else 'AI'

if current_player == 'AI':
    # AI plays center field
    game[1][1] = 'X'
    display_board(game)
    # AI plays best move
    #draw_comp_move(game)
else:
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

if current_player == 'player':
    enter_move(game)
    win = victory_for(game, 'O')
    if win is True:
        print('You Won!')

if win is False:
    print('Draw!')
