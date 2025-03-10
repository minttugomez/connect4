"""This module provides functionality for a Connect 4 game playable against AI.
This module does not include user interface but is playable through command line instead."""

import time

class ConnectFour:

    """ Class for handling game logic and game situation.

    Attributes:
        AI: AI that will be playing against the player """

    def __init__(self, AI):

        """ Constuctor for the class. Creates a playable game.

        Args:
            AI: object from AI class """

        self.ai = AI
        self.grid = [[0] * 7 for _ in range(6)]
        self.turn = 0
        self.exit = False

    def run(self):

        """ Main function for running the game. """

        success = False
        self.turn = 1

        while True:
            if self.turn == 1:
                for row in self.grid:
                    print(row)
                try:
                    column = input("Choose column: ")
                    if column is None:
                        continue
                    if column == "exit":
                        self.exit = True
                        break
                    if int(column) not in range(1, 8):
                        print("Invalid input, try again")
                        time.sleep(1)
                        continue
                    if self.grid[0][int(column) - 1] == 0:
                        column = int(column) - 1
                        success = self.play_turn(self.turn, int(column))
                    else:
                        print("Column is full, try a different column")
                        success = False
                        time.sleep(1)

                except ValueError:
                    pass

            elif self.turn == 2:
                column, _ = self.ai.play(self.grid)
                if column in range(0, 7) and self.grid[0][column] == 0:
                    success = self.play_turn(self.turn, column)

            if success:
                if self.check_win(success[0], success[1]):
                    print(f"Winner: {self.turn}")
                    time.sleep(1)
                    for row in self.grid:
                        print(row)
                    time.sleep(1)
                    break
                if self.grid_full():
                    print("No winner. Out of turns")
                    time.sleep(1)
                    break
                self.switch_turn()
                print(f"Player {self.turn}'s turn")
                time.sleep(1)

        input_exit = input("Exit? (yes or no): ")
        if input_exit == "yes":
            self.exit = True

        if not self.exit:
            print("Starting new game")
            time.sleep(1)

            self.reset_grid()
            self.run()

    def play_turn(self, player, column):

        """ If selected move is accepted, the marker will be placed in the correct cell.

        Args:
            player: player whose turn is currently on
            column: column the player has chosen for their marker

        Returns:
            True if selected move was accepted
            False if selected move was not accepted """

        if player not in [1, 2]:
            return False

        symbol = player

        if 0 <= column <= 6:
            for row in range(5, -1, -1):
                if self.grid[row][column] == 0:
                    self.grid[row][column] = symbol
                    return (row, column)

        return False

    def switch_turn(self):

        """ Switches the turn to the next player. """

        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
        else:
            raise ValueError

    def check_win(self, row, col):

        """ Checks if current player won the game.

        Returns:
            True if current player won
            False if current player did not win """

        row_start = max(0, row - 3)
        col_start = max(0, col - 3)
        row_end = min(5, row + 3)
        col_end = min(6, col + 3)

        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if self.grid[r][c] == self.turn:
                    if (self.check_direction(r, c, 1, 0) or
                        self.check_direction(r, c, 0, 1) or
                        self.check_direction(r, c, 1, 1) or
                        self.check_direction(r, c, 1, -1)):
                        return True
        return False

    def check_direction(self, row, col, delta_row, delta_col):

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
            if 0 <= r < 6 and 0 <= c < 7 and self.grid[r][c] == self.turn:
                count += 1
            else:
                break

        return count == 4

    def grid_full(self):

        """ Checks if the grid is full.
        
        Returns:
            True if grid is full
            False if grid is not full """

        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return False

        return True

    def reset_grid(self):

        """ Resets grid back to the default state. """

        self.grid = [[0] * 7 for _ in range(6)]
