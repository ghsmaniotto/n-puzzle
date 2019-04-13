import numpy
import random


class Board:
    """ Class that represents the n-puzzle board and it methods.

    The two-dimensional matrix that represents the board is like:
     (goal board)       (x and y positions)
      [0][1][2]       [(0,0)] [(0,1)] [(0,2)]
      [3][4][5]   =>  [(1,0)] [(1,1)] [(1,2)]
      [6][7][8]       [(2,0)] [(2,1)] [(2,2)]
    """
    def __init__(self, board_length):
        """ Builld a n-puzzle board.

        Keyword arguments:
        board_length -- number of columns and rows of the board (ex: 3)
        """
        # Number of rows or columns, like: 3
        self.length = board_length
        # Number of board size, like: 3x3 = 9
        self.__size = self.length * self.length
        # Two-dimensional array of length x lenght size
        self.board = self.__initialize_board(board_length)
        # The board that we would like to achieve
        self.__goal_board = self.__initialize_board(board_length)
        # Define the x and y for the empty piece
        self.empty_position = {'x': 0, 'y': 0}

    def print_board(self):
        print(self.board)

    def available_movements(self):
        """ List the available movements in the board for empty space. """
        move_to = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        random.shuffle(move_to)  # Sort movements randomly
        return list(filter(lambda x: self.__valid_movement(x), move_to))

    def move(self, command):
        """ Moves the empty piece for gived command.

        Keyword arguments:
        command -- direction of movement, like: LEFT, RIGHT, UP or DOWN
        """
        # Checks if it is a valid command
        if not self.__valid_movement(command):
            return
        self.__move_empty_position_to(command)

    def randomize(self, moves_count):
        """ Makes moves_count movements randomly in the board.

        Keyword arguments:
        moves_count -- the number of random movements to be done in board
        """
        for _ in range(moves_count):
            move_to = random.sample(self.available_movements(), 1)[0]
            self.move(move_to)

    def is_goal_achieved(self):
        """ Checks if the board is equal to the goal.

        We compare the two-dimensional arrays with the equal operator.
        It returns a True/False two-dimensional array. After that,
        we examine if the count of True positions is equal to board size.

        [0][7][6]    [0][1][2]    [T][F][F]
        [2][4][3] == [3][4][5] -> [F][T][F] -> 3 != 9 (board size)
        [1][5][8]    [6][7][8]    [F][F][T]
        """
        compared_board = self.board == self.__goal_board
        return sum(map(sum, compared_board)) == self.__size

    def difference_to_goal(self):
        """ Returns the number of pieces that are not in the correct position.

        We compare the two-dimensional arrays with the equal operator. 
        It returns a True/False two-dimensional array. After that, 
        we subtract the count of True positions of the board size.
        
        [0][7][6]    [0][1][2]    [T][F][F]
        [2][4][3] == [3][4][5] -> [F][T][F] -> 9 - 3 = 6
        [1][5][8]    [6][7][8]    [F][F][T]
        """
        compared_board = self.board == self.__goal_board
        return self.__size - sum(map(sum, compared_board))

    def sum_of_absolute_differences(self):
        """ Returns the absolute sum of differences of each board position
            and the goal board.

        We get the difference of each position of board and goal board.
        It returns a two-dimensional array with differences of each position.
        After that, we sum the absolute value of differences.

        [0][7][6]    [0][1][2]    [0][+6][+4]
        [2][4][3] -  [3][4][5] -> [-1][0][-2] -> 20
        [1][5][8]    [6][7][8]    [-5][-2][0]
        """
        difference = self.board - self.__goal_board
        return sum(sum(map(lambda x: abs(x), difference)))

    def manhattan_distance(self):
        """ Returns the sum of manhattan distance of each position with the goal

        Manhattan distance equation:
            (|x_1 - x_2|) + (|y_1 - y_2|)

        [0][7][6]  get manhattan  [0][1][2]    [0][2][4]
        [2][4][3]    distance     [3][4][5] -> [3][0][2] -> 13
        [1][5][8]    of goal      [6][7][8]    [2][2][0]
        """
        total_sum = 0
        # For each x and y of board, we calculate it manhattan distance
        #   according to it the goal position
        for x_1, y_1 in numpy.ndindex(self.board.shape):
            # Get x and y value in board
            value = self.board[x_1, y_1]
            # Get x and y for value in goal board
            x_2, y_2 = self.board_index(self.__goal_board, value)
            # Sum to the total, the manhattan distance from position and goal
            total_sum += abs(x_1 - x_2) + abs(y_1 - y_2)
        return total_sum

    def board_index(self, board, value):
        """ Returns board index (x, y) for a given value.

        Keyword arguments:
        board -- two-dimensional array that will search the value
        value -- the searched value

        Example:
        value: 3
                [0][7][6]
        board:  [2][4][3]  
                [1][5][8]
        returns: (1, 2)
        """
        index = numpy.where(board == value)
        return index[0][0], index[1][0]

    def __initialize_board(self, length):
        """ Returns the goal board.

        Keyword arguments:
        length -- the column and row size

        For length returns a two-dimentional array like:
                        [0][1][2]
                        [3][4][5]
                        [6][7][8]
        """
        board = numpy.zeros((length, length))
        start_values = 0
        for x in range(length):
            for y in range(length):
                board[x][y] = start_values
                start_values += 1
        return board

    def __move_to(self, direction):
        """ Returns an object with x and y direction for the movement.

        Keyword arguments:
        direction -- direction for the movement

        The x and y value for the movement is defined according to:
                        [(0,0)] [(0,1)] [(0,2)]
                        [(1,0)] [(1,1)] [(1,2)]
                        [(2,0)] [(2,1)] [(2,2)]
        """
        if direction == 'UP':
            return {'x': -1, 'y': 0}
        elif direction == 'DOWN':
            return {'x': 1, 'y': 0}
        elif direction == 'RIGHT':
            return {'x': 0, 'y': 1}
        elif direction == 'LEFT':
            return {'x': 0, 'y': -1}
        else:
            return {'x': 0, 'y': 0}

    def __valid_movement(self, command):
        """ Checks if the movement is valid.

        Keyword arguments:
        command -- command of movement, like: UP, DOWN, LEFT or RIGHT
        """
        movement_position = self.__move_to(command)
        x = self.empty_position['x'] + movement_position['x']
        y = self.empty_position['y'] + movement_position['y']
        return x < self.length and x >= 0 and y < self.length and y >= 0

    def __move_empty_position_to(self, command):
        """ Move empty position according to command.

        Keyword arguments:
        command -- direction of movement, like: UP, DOWN, LEFT or RIGHT
        """
        direction = self.__move_to(command)
        self.__move(self.empty_position, self.__new_position(direction))

    def __move(self, _from, _to):
        """ Moves in the board the _from position to _to position and vice versa.

        Keyword arguments:
        _from -- object with x and y position
        _to -- object with x and y position
        """
        from_x, from_y, f_value = self.__position_and_value(_from)
        to_x, to_y, to_value = self.__position_and_value(_to)
        self.board[from_x][from_y], self.board[to_x][to_y] = to_value, f_value
        self.empty_position = _to

    def __position_and_value(self, direction):
        """ Returns x, y and value of direction in the board.

        Keyword arguments:
        direction - object with x and y values.

        Example:
        For direction: {x:1, y:1} and board:
                    [0][1][2]
                    [3][4][5]
                    [6][7][8]

        The methods returns: (1, 1, 4)
        """
        x, y = direction['x'], direction['y']
        return x, y, self.board[x][y]

    def __new_position(self, direction):
        """ Calculates new position for empty_piece according a direction.

        Keyword arguments:
        direction -- object with x and y values.

        Example:
            For direction: {x:0, y:-1} and empty piece in {x:1, y:1},
        it returns {x:1, y:0}
        """
        direction['x'] += self.empty_position['x']
        direction['y'] += self.empty_position['y']
        return direction
