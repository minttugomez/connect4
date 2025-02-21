"""This module provides AI for Connect 4.
This AI uses minimax algorithm with alpha-beta pruning to evaluate the best possible moves."""

import time

class AI:

    """ Class for Connect Four AI."""

    def __init__(self):

        """ Constructor for the class. """

        self.columns = [3,2,4,1,5,0,6]
        self.last_cell = (-1, -1)
        self.time_limit = 5
        self.best_moves = {}
        self.start_time = None

    def play(self, grid):

        """ Function for AI playing a turn.
            Runs the minimax algorithm until time limit has been reached.

        Args:
            grid: current game situation in grid form

        Returns:
            best_col: the column where the AI has chosen to place the next marker """

        self.start_time = time.time()

        best_col = None
        for depth in range(1, 100):
            if time.time() - self.start_time > self.time_limit:
                break
            _, col = self.minimax(grid, depth, float('-inf'), float('inf'), is_maximizing=True)
            if col is not None:
                best_col = col
                self.best_moves[self.hash_grid(grid)] = col

        return best_col

    def minimax(self, grid, depth, alpha, beta, is_maximizing):

        """ Minimax algorithm with alpha-beta pruning.
            Evaluates potential moves to determine the best possible move.

        Args:
            grid: current or simulated game situation in grid form
            depth: remaining depth to explore in the game tree
            alpha: best score the maximizer can guarantee so far
            beta: best score the minimizer can guarantee so far
            is_maximizing: indicates whether the current player is the
                           maximizer (AI) or minimizer (opponent)

        Returns:
            score: evaluated score of the move at this depth
            best_col: column index of the best move found at this depth  """

        if time.perf_counter() - self.start_time > self.time_limit:
            timeout = True
        else: timeout = False

        if depth == 0 or self.check_win(self.last_cell[0], self.last_cell[1], grid) or not self.get_valid_columns(grid):
            return self.evaluate_grid(grid), None

        valid_columns = self.get_valid_columns(grid)
        hash_grid = self.hash_grid(grid)
        best = self.best_moves.get(hash_grid)
        if best is not None:
            valid_columns.remove(best)
            valid_columns.insert(0, best)

        if is_maximizing:
            max_score = float('-inf')
            best_col = None
            for col in valid_columns:
                temp_grid = self.simulate_move(grid, col, 2)
                if self.check_win(self.last_cell[0], self.last_cell[1], temp_grid):
                    return 1000, col
                if not timeout:
                    score, column = self.minimax(temp_grid, depth-1, alpha, beta, False)
                    self.best_moves[self.hash_grid(temp_grid)] = column
                    if score > max_score:
                        max_score = score
                        best_col = col
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            return max_score, best_col

        else:
            min_score = float('inf')
            best_col = None
            for col in valid_columns:
                temp_grid = self.simulate_move(grid, col, 1)
                if self.check_win(self.last_cell[0], self.last_cell[1], temp_grid):
                    return -1000, col
                if not timeout:
                    score, column = self.minimax(temp_grid, depth-1, alpha, beta, True)
                    self.best_moves[self.hash_grid(temp_grid)] = column
                    if score < min_score:
                        min_score = score
                        best_col = col
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            return min_score, best_col

    def get_valid_columns(self, grid):

        """ Returns a list of valid columns
        
        Args:
            grid: current or simulated game situation in grid form
        
        Returns:
            valid_columns: columns that are not already full """


        valid_columns = [col for col in self.columns if grid[0][col] == 0]
        return valid_columns

    def simulate_move(self, grid, col, player):

        """ Edits the grid based on a simulated move.
            Updates the marker for the last move made.
        
        Args:
            grid: current or simulated game situation in grid form
            col: chosen column for the simulated move
            player: player whose turn is being simulated
        
        Returns:
            grid: grid updated with the simulated move """

        temp_grid = [row[:] for row in grid]

        for r in range(5, -1, -1):
            if temp_grid[r][col] == 0:
                temp_grid[r][col] = player
                self.last_cell = (r, col)
                break

        return temp_grid

    def evaluate_grid(self, grid):

        """ Checks if current game situation is a win
        
        Args:
            grid: current or simulated game situation in grid form
        
        Returns:
            grid value 1000 if AI wins, -1000 if opponent wins, 0 otherwise """

        if self.check_win(self.last_cell[0], self.last_cell[1], grid):
            if grid[self.last_cell[0]][self.last_cell[1]] == 2:
                return 1000
            else:
                return -1000
        return 0

    def check_win(self, row, col, grid):

        """ Checks if a specific move causes a win

        Args:
            row: row of the last move
            col: column of the last move
            grid: current or simulated game situation in grid form

        Returns:
            True if move causes a win
            False if move doesn't cause a win """

        player = grid[row][col]
        if player == 0:
            return False

        if row == col == -1:
            return False

        row_start = max(0, row - 3)
        col_start = max(0, col - 3)
        row_end = min(5, row + 3)
        col_end = min(6, col + 3)

        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if grid[r][c] == player:
                    if (self.check_direction(grid, r, c, 1, 0) or
                        self.check_direction(grid, r, c, 0, 1) or
                        self.check_direction(grid, r, c, 1, 1) or
                        self.check_direction(grid, r, c, 1, -1)):
                        return True
        return False

    def check_direction(self, grid, row, col, delta_row, delta_col):

        """ Checks if there are four connected markers starting from speficied cell.

        Args:
            grid: current or simulated game situation in grid form
            row: row index of the cell currently being checked
            col: column index of the cell currently being check
            delta_row: vertical direction
                -1 = row above, 0 = same row, 1 = row below
            delta_col: horizontal direction
                -1 = left side column, 0 = same column, 1 = right side column

        Returns:
            True if win row was found
            False if no win row was found """

        player = grid[row][col]
        if player == 0:
            return False
        count = 0

        for i in range(4):
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < 6 and 0 <= c < 7 and grid[r][c] == player:
                count += 1
            else:
                break

        return count == 4

    def hash_grid(self, grid):

        """ Turns grid into a hash table.
        
        Args:
            grid: current or simulated game situation in grid form
        
        Return:
            grid in hash table form"""

        return tuple(tuple(row) for row in grid)
