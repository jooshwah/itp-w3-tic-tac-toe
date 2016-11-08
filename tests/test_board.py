import unittest

from tic_tac_toe.game import Board


EMPTY_BOARD = """
     |     |
  -  |  -  |  -
_____|_____|_____
     |     |
  -  |  -  |  -
_____|_____|_____
     |     |
  -  |  -  |  -
     |     |
"""


NOT_EMPTY_BOARD = """
     |     |
  X  |  -  |  -
_____|_____|_____
     |     |
  -  |  O  |  X
_____|_____|_____
     |     |
  O  |  -  |  -
     |     |
"""


class BoardTestCase(unittest.TestCase):
    def test_make_move_on_board(self):
        board = Board()
        board.move('X', 0, 0)
        board.move('O', 1, 0)
        board.move('X', 1, 1)
        board.move('O', 2, 1)
        board.move('X', 2, 2)

        row_0 = board.get_row(0)
        self.assertEqual(row_0, ['X', None, None])

        row_1 = board.get_row(1)
        self.assertEqual(row_1, ['O', 'X', None])

        row_2 = board.get_row(2)
        self.assertEqual(row_2, [None, 'O', 'X'])

    def test_get_rows(self):
        board = Board([
            ['X', None, None],
            ['O', 'X', None],
            [None, 'O', 'X'],
        ])

        row_0 = board.get_row(0)
        self.assertEqual(row_0, ['X', None, None])

        row_1 = board.get_row(1)
        self.assertEqual(row_1, ['O', 'X', None])

        row_2 = board.get_row(2)
        self.assertEqual(row_2, [None, 'O', 'X'])

    def test_get_columns(self):
        board = Board([
            ['X', None, 'X'],
            [None, 'O', 'X'],
            ['O', None, None],
        ])

        col_0 = board.get_column(0)
        self.assertEqual(col_0, ['X', None, 'O'])

        col_1 = board.get_column(1)
        self.assertEqual(col_1, [None, 'O', None])

        col_2 = board.get_column(2)
        self.assertEqual(col_2, ['X', 'X', None])

    def test_get_diagonals(self):
        board = Board([
            ['X', None, 'X'],
            ['O', 'X', None],
            [None, 'O', 'O'],
        ])

        diagonal_0 = board.get_diagonal(0)
        self.assertEqual(diagonal_0, ['X', 'X', 'O'])

        diagonal_1 = board.get_diagonal(1)
        self.assertEqual(diagonal_1, ['X', 'X', None])

    def test_empty_board_string(self):
        board = Board()
        self.assertEqual(str(board), EMPTY_BOARD)

    def test_not_empty_board_string(self):
        board = Board([
            ['X', None, None],
            [None, 'O', 'X'],
            ['O', None, None],
        ])
        self.assertEqual(str(board), NOT_EMPTY_BOARD)
