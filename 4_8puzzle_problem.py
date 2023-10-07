import heapq
import copy

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]

# Define moves: Up, Down, Left, Right
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
move_names = ['Left', 'Right', 'Up', 'Down']  # Corrected move names


# Helper function to count inversions in the puzzle
def get_inversion_count(puzzle):
    inversion_count = 0
    flat_puzzle = [j for sub in puzzle for j in sub if j != -1]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversion_count += 1
    return inversion_count


# Helper function to check if the puzzle is solvable
def is_solvable(puzzle):
    inversion_count = get_inversion_count(puzzle)
    return inversion_count % 2 == 0


# Helper function to find the position of the empty tile
def find_empty_tile(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                return i, j


# Helper function to calculate the number of misplaced tiles
def misplaced_tiles(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal_state[i][j] and board[i][j] != -1:
                count += 1
    return count


# A* search function
def solve_puzzle(initial_state):
    visited = set()
    priority_queue = []

    inversion_count = get_inversion_count(initial_state)  # Get inversion count at the start

    if not is_solvable(initial_state):
        return None  # Puzzle is unsolvable

    # Create a tuple with the initial state, its cost, and a sequence of moves
    initial_cost = inversion_count + misplaced_tiles(initial_state)  # Include inversion count in initial cost
    heapq.heappush(priority_queue, (initial_cost, 0, initial_state, []))

    while priority_queue:
        _, cost, current_state, moves_so_far = heapq.heappop(priority_queue)
        visited.add(tuple(map(tuple, current_state)))  # Convert the board to a tuple for hashing

        if current_state == goal_state:
            return moves_so_far

        x, y = find_empty_tile(current_state)

        for move, move_name in zip(moves, move_names):
            dx, dy = move
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = copy.deepcopy(current_state)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                if tuple(map(tuple, new_state)) not in visited:
                    new_inversion_count = get_inversion_count(new_state)  # Calculate inversion count for the new state
                    new_cost = cost + 1 + new_inversion_count + misplaced_tiles(new_state)
                    new_moves = moves_so_far + [move_name]
                    heapq.heappush(priority_queue, (new_cost, cost + 1, new_state, new_moves))

    return None  # No solution found


# Test the solver
# initial_state = [[8, 1, 2], [-1, 4, 3], [7, 6, 5]]                 # not possible
initial_state = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]                 # easy
# initial_state = [[1, 8, 2], [-1, 4, 3], [7, 6, 5]]                 # hard
solution = solve_puzzle(initial_state)

# Print the number of inversions at the start
print("Initial Inversion Count:", get_inversion_count(initial_state))

if solution:
    print("Solution found in", len(solution), "moves:")
    for i, move in enumerate(solution, start=1):
        for row in initial_state:
            print(" ".join(map(str, row)))
        print("Step", i, ":", move)
        print()
        # Apply the move to update the initial state for the next step
        dx, dy = moves[move_names.index(move)]
        x, y = find_empty_tile(initial_state)
        initial_state[x][y], initial_state[x + dx][y + dy] = initial_state[x + dx][y + dy], initial_state[x][y]

    # Print the goal state at the end
    print("Goal State:")
    for row in goal_state:
        print(" ".join(map(str, row)))
else :
    print("No solution exists.")
