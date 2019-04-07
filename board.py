import numpy
import random


class Board:
    def __init__(self, board_length):
        self.length = board_length
        self.board = self.__initialize_board(board_length)
        self.empty_position = {'x': 0, 'y': 0}

    def print_board(self):
        print(self.board)

    def available_movements(self):
        move_to = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        return list(filter(lambda x: self.__valid_movement(x), move_to))

    def move(self, command):
        print(command)
        if not self.__valid_movement(command):
            print('Invalid movement')
            return
        self.__move_empty_position_to(command)

    def __initialize_board(self, length):
        board = numpy.zeros((length, length))
        start_values = 0
        for x in range(length):
            for y in range(length):
                board[x][y] = start_values
                start_values += 1
        return board

    def __empty_box_position(self):
        return self.empty_position['x'], self.empty_position['y']

    def __move_to(self, direction):
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

    def __valid_movement(self, movement):
        movement_position = self.__move_to(movement)
        x = self.empty_position['x'] + movement_position['x']
        y = self.empty_position['y'] + movement_position['y']
        return x < self.length and x >= 0 and y < self.length and y >= 0

    def __move_empty_position_to(self, command):
        direction = self.__move_to(command)
        self.__move(self.empty_position, self.__new_position(direction))

    def __move(self, _from, _to):
        from_x, from_y, f_value = self.__position_and_value(_from)
        to_x, to_y, to_value = self.__position_and_value(_to)
        self.board[from_x][from_y], self.board[to_x][to_y] = to_value, f_value
        self.empty_position = _to

    def __position_and_value(self, direction):
        x, y = direction['x'], direction['y']
        return x, y, self.board[x][y]

    def __new_position(self, direction):
        direction['x'] += self.empty_position['x']
        direction['y'] += self.empty_position['y']
        return direction
