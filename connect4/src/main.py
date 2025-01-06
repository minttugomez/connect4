"""This module initializes connect4 and AI objects and launches the Connect 4 game."""

from connect4 import ConnectFour
from AI import AI

ai = AI()
connect4 = ConnectFour(ai)

connect4.run()
