import unittest
from unittest.mock import Mock
from connect4 import ConnectFour

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.mock_AI = Mock()
        self.connect_four = ConnectFour(self.mock_AI)

    def test_play_turn_invalid_player(self):
        player = 0
        self.assertFalse(self.connect_four.play_turn(player, 0))

    def test_play_turn_valid(self):
        player = 1
        column = 1
        self.assertTrue(self.connect_four.play_turn(player, column))
        self.assertEqual(self.connect_four.grid[5][column], player)

    def test_play_turn_invalid(self):
        player = 1
        column = 1
        for _ in range(6):
            self.connect_four.play_turn(2, column)
        self.assertFalse(self.connect_four.play_turn(player, column))
        self.assertEqual(self.connect_four.grid[0][column], 2)

    def test_play_turn_out_of_range(self):
        player = 1
        column = 8
        self.assertFalse(self.connect_four.play_turn(player, column))
        self.assertEqual(self.connect_four.grid[5][6], 0)

    def test_switch_turn(self):
        self.connect_four.turn = 1
        self.connect_four.switch_turn()
        self.assertEqual(self.connect_four.turn, 2)
        self.connect_four.switch_turn()
        self.assertEqual(self.connect_four.turn, 1)
    
    def test_switch_turn_invalid(self):
        self.connect_four.turn = 3
        with self.assertRaises(ValueError):
            self.connect_four.switch_turn()
    
    def test_check_win_horizontal(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 1, 1, 1, 0, 0],
                                  [0, 2, 2, 2, 1, 0, 0],
                                  [0, 2, 1, 2, 2, 0, 0],
                                  [0, 1, 2, 2, 1, 0, 0]]
        self.assertTrue(self.connect_four.check_win(2, 2))

    def test_check_win_vertical(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [0, 2, 0, 0, 0, 0, 0]]
        self.assertTrue(self.connect_four.check_win(1, 1))

    def test_check_win_diagonal_1(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 2, 1, 0, 0, 0],
                                  [0, 0, 2, 2, 1, 0, 0],
                                  [0, 0, 2, 1, 1, 1, 0]]
        self.assertTrue(self.connect_four.check_win(5, 5))

    def test_check_win_diagonal_2(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 1],
                                  [0, 0, 0, 0, 0, 1, 1],
                                  [0, 0, 0, 0, 1, 1, 2],
                                  [0, 0, 0, 1, 2, 2, 2],
                                  [0, 0, 0, 2, 1, 2, 1]]
        self.assertTrue(self.connect_four.check_win(1, 6))

    def test_check_win_no_win(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 1, 0, 0, 0, 0, 0],
                                  [0, 2, 0, 0, 0, 0, 0],
                                  [0, 1, 2, 0, 1, 1, 0],
                                  [0, 2, 2, 2, 1, 1, 0],
                                  [0, 2, 1, 2, 1, 2, 0],
                                  [0, 1, 2, 2, 2, 1, 0]]
        self.assertFalse(self.connect_four.check_win(2, 4))

    def test_grid_full(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[2, 1, 1, 1, 2, 2, 2],
                                  [2, 1, 1, 2, 1, 2, 1],
                                  [1, 1, 1, 2, 1, 1, 1],
                                  [2, 2, 2, 1, 1, 2, 1],
                                  [2, 2, 1, 1, 2, 2, 2],
                                  [2, 1, 2, 2, 2, 1, 1]]
        self.assertTrue(self.connect_four.grid_full())

    def test_grid_not_full(self):
        self.connect_four.turn = 1
        self.connect_four.grid = [[0, 1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0],
                                  [2, 2, 0, 0, 0, 0, 2],
                                  [1, 2, 1, 0, 2, 0, 1],
                                  [2, 1, 2, 0, 2, 2, 2]]
        self.assertFalse(self.connect_four.grid_full())

    def test_reset_grid(self):
        expected_grid = [[0] * 7 for _ in range(6)]
        self.connect_four.grid = [[1] * 7 for _ in range(6)]
        self.connect_four.reset_grid()

        self.assertEqual(self.connect_four.grid, expected_grid)
