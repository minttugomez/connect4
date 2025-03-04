import unittest
from unittest.mock import Mock
from AI import AI

class TestAI(unittest.TestCase):
    def setUp(self):
        self.AI = AI()

    def test_init(self):
        self.assertEqual(self.AI.columns, [3,2,4,1,5,0,6])
        self.assertEqual(self.AI.last_cell, (-1, -1))
        self.assertEqual(self.AI.time_limit, 5)
        self.assertEqual(self.AI.best_moves, {})
        self.assertEqual(self.AI.start_time, None)

    def test_play(self):
        grid = [[0, 0, 0, 0, 0, 0, 0] for _ in range(6)]
        self.AI.time_limit = 0.1
        best_col, _ = self.AI.play(grid)
        self.assertIsNotNone(best_col)

    def test_play_for_win(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1, 2],
                [0, 0, 0, 2, 2, 2, 1],
                [0, 0, 1, 2, 1, 2, 1]]
        best_col, _ = self.AI.play(grid)
        self.assertEqual(best_col, 2)

    def test_win_in_five_moves(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0],
                [0, 0, 0, 2, 2, 0, 0],
                [0, 0, 2, 1, 2, 1, 0],
                [1, 0, 1, 2, 1, 1, 2]]
        best_col, score = self.AI.play(grid)
        self.assertEqual(best_col, 5)
        self.assertEqual(score, 1000)

    def test_avoid_loss(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 1, 2, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 2, 0, 0, 0]]
        best_col, _ = self.AI.play(grid)
        self.assertEqual(best_col, 2)

    def test_evaluate_grid_win(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1, 2],
                [0, 0, 2, 2, 2, 2, 1],
                [0, 0, 1, 2, 1, 2, 1]]
        self.AI.last_cell = (4, 2)
        self.assertEqual(self.AI.evaluate_grid(grid), 1000)

    def test_evaluate_grid_enemy_win(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1, 2],
                [0, 0, 2, 1, 2, 2, 1],
                [0, 0, 1, 2, 1, 2, 1]]
        self.AI.last_cell = (4, 3)
        self.assertEqual(self.AI.evaluate_grid(grid), -1000)

    def test_evaluate_grid_no_win(self):
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1, 2],
                [0, 0, 2, 0, 2, 2, 1],
                [0, 0, 1, 2, 1, 2, 1]]
        self.AI.last_cell = (4, 2)
        self.assertEqual(self.AI.evaluate_grid(grid), 0)
