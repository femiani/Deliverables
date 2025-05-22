import random

# Define the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_tie(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def ai_move(board):
    moves = get_available_moves(board)
    return random.choice(moves)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == 'X':
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        else:
            row, col = ai_move(board)
            print(f"AI chooses: {row}, {col}")

        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_tie(board):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Call the main game loop
if __name__ == "__main__":
    main()
