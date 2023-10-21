#                IMPLEMENT CSP,SOLVING N-QUEEN PROBLEM USING BACKTRACKING
def is_safe(board, row, col, N):
    # Check if a queen can be placed at the given row and column
    # without conflicting with existing queens.

    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_n_queens_util(board, 0, N, solutions)

    if not solutions:
        print("No solutions exist for N =", N)
    else:
        print(f"Found {len(solutions)} solution(s) for N = {N}:")
        for idx, solution in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            print_solution(solution, N)
            print()


def solve_n_queens_util(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, solutions)
            board[i][col] = 0


# Example usage
# N = 4  # You can change N to any positive integer
N_queens = int(input("Enter N for N-Queens problem : "))
solve_n_queens(N_queens)
#    MADE BY ABHISHEK
