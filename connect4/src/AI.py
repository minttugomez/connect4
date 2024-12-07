class AI:

    """ Class for Connect Four AI. """

    def __init__(self):

        """ Constructor for the class. """

        self.columns = [3,2,4,1,5,0,6]

    def play(self, grid):

        """ Function for playing a turn.
            Run through ConnectFour class when it's the AI's turn.

        Args:
            grid: current game situation in grid form

        Returns:
            column: the column where the AI has chosen to place the next marker """

        free = self.get_valid_columns(grid)
        column = free[0]
        for col in free:
            if self.check_win(col, grid):
                column = col
                break

        return column
    
    def get_valid_columns(self, grid):
        
        """ Returns a list of valid columns
        
        Args:
            grid: current game situation in grid form
        
        Returns:
            valid_columns: columns that are not already full """
        

        valid_columns = [col for col in self.columns if grid[0][col] == 0]
        return valid_columns

    def check_win(self, col, grid):

        """ Checks if a specific move will cause a win

        Returns:
            True if move causes a win
            False if move doesn't cause a win """

        test_grid = [row[:] for row in grid]

        for r in range(5, -1, -1):
            if test_grid[r][col] == 0:
                row = r
                break

        test_grid[row][col] = 2

        row_start = max(0, row - 3)
        col_start = max(0, col - 3)
        row_end = min(5, row + 3)
        col_end = min(6, col + 3)

        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if test_grid[r][c] == 2:
                    if (self.check_direction(test_grid, r, c, 1, 0) or
                        self.check_direction(test_grid, r, c, 0, 1) or
                        self.check_direction(test_grid, r, c, 1, 1) or
                        self.check_direction(test_grid, r, c, 1, -1)):
                        return True
        return False

    def check_direction(self, test_grid, row, col, delta_row, delta_col):

        """ Checks if there are four connected markers starting from speficied cell.

        Args:
            row: row index of the cell currently being checked
            col: column index of the cell currently being check
            delta_row: vertical direction
                -1 = row above, 0 = same row, 1 = row below
            delta_col: horizontal direction
                -1 = left side column, 0 = same column, 1 = right side column

        Returns:
            True if win row was found
            False if no win row was found """

        count = 0

        for i in range(4):
            r = row + i * delta_row
            c = col + i * delta_col
            if 0 <= r < 6 and 0 <= c < 7 and test_grid[r][c] == 2:
                count += 1
            else:
                break

        return count == 4