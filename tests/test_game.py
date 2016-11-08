import unittest

from tic_tac_toe.game import Game, Board
from tic_tac_toe.exceptions import InvalidMovementException


class GameInterfaceTestCase(unittest.TestCase):
    def test_create_a_game_and_public_interface(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        self.assertFalse(game.is_finished())
        self.assertFalse(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertIsNone(game.get_winner())

        self.assertEqual(game.next_turn(), 'X')

        self.assertEqual(game.board, board)

    def test_check_winner_returns_false(self):
        board = Board([
            [None, None, None],
            ['X', None, 'O'],
            [None, 'X', None],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertFalse(game.is_finished())
        self.assertFalse(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertIsNone(game.get_winner())

    def test_check_winner_returns_true_for_row(self):
        board = Board([
            [None, None, None],
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertTrue(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertEqual(game.get_winner(), 'X')

    def test_check_winner_returns_true_for_column(self):
        board = Board([
            ['X', None, None],
            ['X', None, None],
            ['X', 'O', 'O'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertTrue(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertEqual(game.get_winner(), 'X')

    def test_check_winner_returns_true_first_diagonal(self):
        board = Board([
            ['X', None, None],
            ['O', 'X', None],
            [None, 'O', 'X'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertTrue(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertEqual(game.get_winner(), 'X')

    def test_check_winner_returns_true_second_diagonal(self):
        board = Board([
            [None, None, 'X'],
            [None, 'X', None],
            ['X', 'O', 'O'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertTrue(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertEqual(game.get_winner(), 'X')

    def test_game_is_tied(self):
        board = Board([
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertFalse(game.has_winner())
        self.assertTrue(game.is_tied())
        self.assertIsNone(game.get_winner())


class GameMoveTestCase(unittest.TestCase):
    def test_game_makes_valid_moves(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        # === First Move ===
        self.assertEqual(game.next_turn(), 'X')
        game.move('X', row=0, col=0)

        row_0 = game.board.get_row(0)
        self.assertEqual(row_0, ['X', None, None])

        row_1 = game.board.get_row(1)
        self.assertEqual(row_1, [None, None, None])

        row_2 = game.board.get_row(2)
        self.assertEqual(row_2, [None, None, None])

        # === Second Move ===
        self.assertEqual(game.next_turn(), 'O')
        game.move('O', row=1, col=1)

        row_0 = game.board.get_row(0)
        self.assertEqual(row_0, ['X', None, None])

        row_1 = game.board.get_row(1)
        self.assertEqual(row_1, [None, 'O', None])

        row_2 = game.board.get_row(2)
        self.assertEqual(row_2, [None, None, None])

        # === Third Move ===
        self.assertEqual(game.next_turn(), 'X')
        game.move('X', row=2, col=1)

        row_0 = game.board.get_row(0)
        self.assertEqual(row_0, ['X', None, None])

        row_1 = game.board.get_row(1)
        self.assertEqual(row_1, [None, 'O', None])

        row_2 = game.board.get_row(2)
        self.assertEqual(row_2, [None, 'X', None])

    def test_invalid_move_not_players_turn(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        self.assertEqual(game.next_turn(), 'X')
        with self.assertRaises(InvalidMovementException):
            game.move('O', row=0, col=0)

    def test_invalid_move_position_already_taken(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        self.assertEqual(game.next_turn(), 'X')
        game.move('X', row=0, col=0)

        self.assertEqual(game.next_turn(), 'O')
        with self.assertRaises(InvalidMovementException):
            game.move('O', row=0, col=0)

    def test_invalid_move_invalid_positions(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        self.assertEqual(game.next_turn(), 'X')

        with self.assertRaises(InvalidMovementException):
            game.move('X', row=3, col=0)

        with self.assertRaises(InvalidMovementException):
            game.move('X', row=0, col=3)

        with self.assertRaises(InvalidMovementException):
            game.move('X', row=-1, col=0)

    def test_invalid_move_invalid_player(self):
        board = Board()
        game = Game(board=board, player_1='X', player_2='O')

        self.assertEqual(game.next_turn(), 'X')
        with self.assertRaises(InvalidMovementException):
            game.move('L', row=0, col=0)

    def test_invalid_move_game_over_game_is_tied(self):
        board = Board([
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X'],
        ])
        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertFalse(game.has_winner())
        self.assertTrue(game.is_tied())
        self.assertIsNone(game.get_winner())

        with self.assertRaises(InvalidMovementException):
            game.move('X', row=0, col=0)

    def test_invalid_move_game_has_winner(self):
        board = Board([
            ['X', None, None],
            ['O', 'X', None],
            [None, 'O', 'X'],
        ])

        game = Game(board=board, player_1='X', player_2='O')

        self.assertTrue(game.is_finished())
        self.assertTrue(game.has_winner())
        self.assertFalse(game.is_tied())
        self.assertEqual(game.get_winner(), 'X')

        self.assertEqual(game.next_turn(), 'X')
        with self.assertRaises(InvalidMovementException):
            game.move('X', row=0, col=2)
