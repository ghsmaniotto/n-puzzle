from board import Board
from tree import Tree
import time


# Open results.txt file to write the results
result_file = open("results.txt", "w")
# Define the header of csv file
result_file.write('size,movements,strategy,time,out,memory\n')

# Define the board length
N = [3, 4, 5]
# Define how many movements will be done randonly until to be the initial board state
MOVES_TO_RANDOMIZE = [10, 30, 50, 100]
# Define the tree search algorithms
STRATEGIES = ['DSF', 'BSF', 'IDS', 'A_STAT_A', 'A_STAR_B', 'A_STAR_MANHATTAN']

# Define how many times will execute each configuration
for _ in range(5):
    for size in N:
        for randomize_moves in MOVES_TO_RANDOMIZE:
            # Create board according to size
            board = Board(size)
            # Randomize the board according move counts
            board.randomize(randomize_moves)

            for strategy in STRATEGIES:
                decision_tree = Tree(board)
                # Start count time for solving the problem
                start = time.time()
                # Choose the strategy solution
                if strategy == 'DSF':
                    out = decision_tree.BFS()
                elif strategy == 'BSF':
                    out = decision_tree.DFS()
                elif strategy == 'IDS':
                    out = decision_tree.IDS()
                elif strategy == 'A_STAT_A':
                    out = decision_tree.A_star(
                            lambda x: decision_tree.heuristic_a(x))
                elif strategy == 'A_STAR_B':
                    out = decision_tree.A_star(
                            lambda x: decision_tree.heuristic_b(x))
                elif strategy == 'A_STAR_MANHATTAN':
                    out = decision_tree.A_star(
                            lambda x: decision_tree.manhattan_distance(x))
                else:
                    pass
                # Ends the execution time
                end = time.time()

                # Add result as row in results file
                result_file.write('{},{},{},{},{},{}\n'.format(
                    size,
                    randomize_moves,
                    strategy,
                    end - start,
                    out,
                    decision_tree.size))
