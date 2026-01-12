def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    try:
        while True:
            print_board(board)

            # If there's a winner, the winner is the previous player
            if check_winner(board):
                winner = "O" if player == "X" else "X"
                print_board(board)
                print("Player " + winner + " wins!")
                break

            # Check for draw (board full, no winner)
            if all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a draw!")
                break

            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            except ValueError:
                print("Invalid input; please enter integers 0, 1, or 2.")
                continue

            # Validate coordinates range
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. Goodbye!")


tic_tac_toe()