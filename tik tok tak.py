import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tik-Tok-Tak!")
    print_board(board)

    while True:
        if current_player == 'X':
            row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, 2) separated by space: ").split())
        else:
            print("Computer's turn:")
            move = computer_move(board)
            if move:
                row, col = move
                print(f"Computer chose: {row}, {col}")
            else:
                print("It's a tie!")
                break

        if board[row][col] == ' ':
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
