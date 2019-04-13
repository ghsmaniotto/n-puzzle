from node import Node
from board import Board
import copy


class Tree:
    def __init__(self, board):
        self.__head = Node()
        self.__depth = 0
        self.__max_depth = 15
        self.__initial_board = board
        self.size = 0
        self.MAX_SIZE = 100000

    def __inverse(self, first_command, second_command):
        """ Checks if the first_command is inverse of second_command.

        Keyword arguments:
        first_command -- direction for movement like: UP, DOWN, RIGHT or LEFT
        second_command -- direction for movement like: UP, DOWN, RIGHT or LEFT
        """
        if first_command == 'LEFT' and second_command == 'RIGHT':
            return True
        if first_command == 'RIGHT' and second_command == 'LEFT':
            return True
        if first_command == 'UP' and second_command == 'DOWN':
            return True
        if first_command == 'DOWN' and second_command == 'UP':
            return True
        return False

    def __is_inverse(self, node, command):
        """ Checks if the command is the inverse of last command in node

        Keyword arguments:
        node -- tree node
        command -- direction for movement like: UP, DOWN, RIGHT or LEFT
        """
        # Gets node commands
        commands = node.value
        # Checks if the command is inverse of last node command
        return (len(commands) > 0 and self.__inverse(commands[-1], command))

    def insert_node(self, node, value):
        """ Inserts node in the tree.

        Keyword arguments:
        node -- parent node to insert new child
        value -- value of new node
        """
        new_value = list(node.value)
        new_value.append(value)
        # The new node value will be the parent value appended the value
        child = Node(new_value, node.depth)
        node.add_child(child)
        # Increments the count of tree nodes
        self.size += 1
        return child

    def remove_node(self, node, value):
        """ Removes node in the tree.

        Keyword arguments:
        node -- parent node to remove child
        value -- value of new node
        """
        node.remove_child(value)

    def BFS(self):
        """ Execute the BFS (Breath-First Search) search tree algorithm
        in order to return the movement list to solve n-puzzle game.
        """
        # List that store the nodes that need to be visited
        to_visit_nodes = [self.__head]
        # Node that solves the problem
        node = self.__head

        # Search in tree by node that solves the problem while there are nodes
        # to visit or the tree size is greater than maximum defined
        while len(to_visit_nodes) > 0 and self.size < self.MAX_SIZE:
            # Get the last node in the to_visit_nodes array
            current_node = to_visit_nodes.pop()
            # Make copy of initial board
            board = copy.deepcopy(self.__initial_board)

            # Execute node movement in initial board
            for movement in current_node.value:
                board.move(movement)

            # Returs if the node commands achieves the goal
            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            # If the node commands doesn't achieve the goal
            # add node available movements as it childrens
            # and add it to the begin of to_visit_nodes
            for movement in board.available_movements():
                if not self.__is_inverse(current_node, movement):
                    new_node = self.insert_node(current_node, movement)
                    to_visit_nodes.insert(0, new_node)

        return node.value

    def DFS(self):
        """ Execute the DFS (Depth-First Search) search tree algorithm
        in order to return the movement list to solve n-puzzle game.
        """
        # List that store the nodes that need to be visited
        to_visit_nodes = [self.__head]
        # Node that solves the problem
        current_node = node = self.__head

        # Search in tree by node that solves the problem while there are nodes
        # to visit or the tree size is greater than maximum defined
        while len(to_visit_nodes) > 0 and self.size < self.MAX_SIZE:
            # Get the first node in the to_visit_nodes array
            current_node = to_visit_nodes.pop(0)
            # Make copy of initial board
            board = copy.deepcopy(self.__initial_board)

            # Execute node movement in initial board
            for movement in current_node.value:
                board.move(movement)

            # Execute node movement in initial board
            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            # If the node commands doesn't achieve the goal
            # add node available movements as it childrens
            # and add it to the begin of to_visit_nodes
            if current_node.depth < self.__max_depth:
                for movement in board.available_movements():
                    if not self.__is_inverse(current_node, movement):
                        new_node = self.insert_node(current_node, movement)
                        to_visit_nodes.insert(0, new_node)

        return node.value

    def IDS(self):
        """ Execute the IDS (Iterative Depth Search) search tree algorithm
        in order to return the movement list to solve n-puzzle game.
        """
        # List that store the nodes that need to be visited
        to_visit_nodes = [self.__head]
        # Node that solves the problem
        current_node = node = self.__head

        # Search in tree by node that solves the problem while there are nodes
        # to visit or the tree size is greater than maximum defined
        while len(to_visit_nodes) > 0 and self.size < self.MAX_SIZE:
            # Get the first node in the to_visit_nodes array
            current_node = to_visit_nodes.pop(0)
            # Make copy of initial board
            board = copy.deepcopy(self.__initial_board)

            # Execute node movement in initial board
            for movement in current_node.value:
                board.move(movement)

            # Returs if the node commands achieves the goal
            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            # If the node commands doesn't achieve the goal
            # add node available movements as it childrens
            # and add it to the begin of to_visit_nodes
            if current_node.depth < self.__max_depth:
                for movement in board.available_movements():
                    if not self.__is_inverse(current_node, movement):
                        new_node = self.insert_node(current_node, movement)
                        to_visit_nodes.insert(0, new_node)
            # If the max_depth is achieved, increment it value in order to
            # to keep searching for the solution
            else:
                if len(to_visit_nodes) == 1:
                    self.__max_depth += 5

        return node.value

    def A_star(self, heuristic):
        """ Execute the A* search tree algorithm in order to return 
        the movement list to solve n-puzzle game.

        Keyword arguments:
        heuristic -- heuristic method to calculate the a* estimative
        """
        # A list that store a object with the nodes and its heuristic weight
        to_visit_nodes = [
            {'weight': self.__head.depth, 'node': self.__head}
        ]
        # Node that solves the problem
        node = self.__head

        # Search in tree by node that solves the problem while there are nodes
        # to visit or the tree size is greater than maximum defined
        while len(to_visit_nodes) > 0 and self.size < self.MAX_SIZE:
            # Get the first node in the to_visit_nodes array
            current_node = to_visit_nodes.pop(0)['node']
            # Make copy of initial board
            board = copy.deepcopy(self.__initial_board)

            # Execute node movement in initial board
            for movement in current_node.value:
                board.move(movement)

            # Returs if the node commands achieves the goal
            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            # If the node commands doesn't achieve the goal
            # add node available movements as it childrens
            # and add it to the begin of to_visit_nodes
            for movement in board.available_movements():
                if not self.__is_inverse(current_node, movement):
                    new_node = self.insert_node(current_node, movement)
                    heuristic_value = heuristic(board) + new_node.depth
                    # Add object with node and it weight to to_visit_nodes list
                    to_visit_nodes.insert(
                        0, {'weight': heuristic_value, 'node': new_node}
                    )
                    # Sort to_visit_nodes list to keep the minimum weight 
                    # as the first position list
                    to_visit_nodes.sort(key=lambda x: x['weight'])

        return node.value

    def heuristic_a(self, board):
        """ Returns the heuristic value according the board.

        This heuristic method returns the count of pieces that are in
        it correct position according to the goal board.

        Keyword arguments:
        board -- two-dimensional array to be base of heristic method
        """
        return board.difference_to_goal()

    def heuristic_b(self, board):
        """ Returns the heuristic value according the board.

        This heuristic method returns the sum of absolute differences of
        each board position and the equivalent into the goal board.

        Keyword arguments:
        board -- two-dimensional array to be base of heristic method
        """
        return board.sum_of_absolute_differences()

    def manhattan_distance(self, board):
        """ Returns the heuristic value according the board.

        This heuristic method returns the sum of manhattan distance of
        each board position and it correct position in goal board.

        Keyword arguments:
        board -- two-dimensional array to be base of heristic method
        """
        return board.manhattan_distance()
