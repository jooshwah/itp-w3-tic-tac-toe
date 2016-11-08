class Game(object):

    def __init__(self, board, player_1, player_2):
        pass

    def is_finished(self):
        pass

    def has_winner(self):
        pass

    def is_tied(self):
        pass

    def get_winner(self):
        pass

    def next_turn(self):
        pass

    def move(self, player, row, col):
        pass


BOARD_TEMPLATE = """
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
"""


class Board(object):
    def __init__(self, initial_board=None):
        pass

    def move(self, figure, row, col):
        pass

    def __str__(self):
        return BOARD_TEMPLATE  # .format()

    def get_row(self, row_number):
        pass

    def get_column(self, col_number):
        pass

    def get_diagonal(self, row_number):
        pass
