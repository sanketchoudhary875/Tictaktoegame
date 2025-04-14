# Tic Tac Toe Game in Python

def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    # Check if the board is full
    return all(cell != " " for row in board for cell in row)

def play_game():
    # Initialize the game
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Take player input
        try:
            print(f"Player {current_player}'s turn.")
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if board[row][col] != " ":
                print("Cell already taken. Choose a different cell.")
                continue

            # Update the board
            board[row][col] = current_player
            print_board(board)

            # Check for a winner
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            # Check for a draw
            if is_full(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")

if __name__ == "__main__":
    play_game()