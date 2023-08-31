def print_board(board):
    for i, row in enumerate(board):
        row_display = [cell if cell != " " else str(i * 3 + j + 1) for j, cell in enumerate(row)]
        print(" | ".join(row_display))
        if i < 2:
            print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}'s turn. Enter a number (1-9): ")
       
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if board[row][col] != " ":
            print("That position is already taken. Choose a different one.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
