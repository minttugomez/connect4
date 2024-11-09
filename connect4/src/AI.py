import random

class AI:

    """ Class for Connect Four AI. """

    def __init__(self):

        """ Constructor for the class. """

    def play(self, grid):

        """ Function for playing a turn.
            Run through ConnectFour class when it's the AI's turn.

        Args:
            grid: current game situation in grid form

        Returns:
            column: the column where the AI has chosen to place the next marker """

        free = set()

        for i in range(7):
            if grid[0][i] == 0:
                free.add(i)

        print(free)
        column = random.choice(list(free)) + 1

        return column
