def print_board(board):
    # print the current state of the board
    print("  0 1 2")
    for row in range(3):
        print(row, end=" ")
        for col in range(3):
            print(board[row][col], end=" ")
        print()


def check_win(board):
    # check if there's a win on a board
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        # check columns
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def play_game():
    # Initialize the board and the player
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    # Main game loop
    while True:
        # Print the board and ask the player for input
        print_board(board)
        row = int(input("Enter row (0-2) for {}: ".format(player)))
        col = int(input("Enter column (0-2) for {}: ".format(player)))

        # Check if the input is valid
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input! Try again.")
            continue

        elif board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Update the board and check for a win
        board[row][col] = player
        winner = check_win(board)
        if winner is not None:
            print_board(board)
            print("Congratulations, {} wins!".format(winner))
            break

        # Switch to the other player
        player = "O" if player == "X" else "X"

        # Check for a tie
        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a tie")
            break


play_game()
