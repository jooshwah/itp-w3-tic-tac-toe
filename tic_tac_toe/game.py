from .exceptions import InvalidMovementException


class Game(object):
    VALID_POSITIONS = list(range(3))

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

        self.next_player = self.player_1

    def is_finished(self):
        return self.has_winner() or self.is_tied()

    def has_winner(self):
        return self.get_winner() is not None

    def is_tied(self):
        for elem in self.board.flatten():
            if elem is None:
                return False
        return True

    def get_winner(self):
        # import ipdb; ipdb.set_trace()
        valid_combinations = [
            self.board.get_row(i) for i in range(3)
        ] + [
            self.board.get_diagonal(i) for i in range(2)
        ] + [
            self.board.get_column(i) for i in range(3)
        ]
        for combination in valid_combinations:
            elems = set(combination)
            if None not in elems and len(elems) == 1:
                return combination[0]

        return None

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        invalid_move_condition = (
            player != self.next_player or
            row not in self.VALID_POSITIONS or
            col not in self.VALID_POSITIONS or
            self.board.get_row(row)[col] is not None or
            self.is_finished()
        )
        if invalid_move_condition:
            raise InvalidMovementException()

        self.board.move(player, row, col)
        self.next_player = 'X' if player == 'O' else 'O'


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
    def _get_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __init__(self, initial_board=None):
        self._board = initial_board or self._get_empty_board()

    def move(self, figure, row, col):
        self._board[row][col] = figure

    def flatten(self):
        return [item for sublist in self._board for item in sublist]

    def __str__(self):
        # return BOARD_TEMPLATE.format(*(
        #     [val or '-' for val in self._board[0]] +
        #     [val or '-' for val in self._board[1]] +
        #     [val or '-' for val in self._board[2]]
        # ))

        flatten_board = [
            item or '-' for sublist in self._board for item in sublist]
        return BOARD_TEMPLATE.format(*flatten_board)

    def get_row(self, row_number):
        return self._board[row_number]

    def get_column(self, col_number):
        # 0: 00, 10, 20
        # 1: 01, 11, 21
        # 2: 02, 12, 22
        return [self._board[i][col_number] for i in range(3)]

    def get_diagonal(self, row_number):
        # Diagonal indexes
        # 0: 00, 11, 22
        # 1: 02, 11, 20
        indexes = [
            (0, row_number * 2),
            (1, 1),
            (2, 2 - (row_number * 2))
        ]
        return [self._board[r][c] for r, c in indexes]
