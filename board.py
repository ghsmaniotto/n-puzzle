import numpy

class Board:
  def __init__(self, board_length):
    self.length = board_length
    self.board = self.__initialize_board(board_length)

  def __initialize_board(self, length):
    board = numpy.zeros((length, length))
    start_values = 0
    for i in range(length):
      for j in range(length):
        board[i][j] = start_values
        start_values += 1
    return board
