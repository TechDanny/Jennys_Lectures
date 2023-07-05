import sys


    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    # Recursive function to solve the N queens problem

    # Base case: If all queens are placed, print the solution
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen at position (i, col)
            board[i][col] = 1

            # Recur for the next column
            solve_n_queens(board, col + 1)

            # Backtrack and remove the queen from position (i, col)
            board[i][col] = 0


def print_solutions():
    # Print all the solutions
    for solution in solutions:
        for row, col in solution:
            print("[{}, {}]".format(row, col), end=" ")
        print()


# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is greater or equal to 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

# List to store the solutions
solutions = []

# Solve the N queens problem
solve_n_queens(board, 0)

# Print the solutions
print_solutions()

