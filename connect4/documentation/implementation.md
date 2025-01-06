# Implementation document for Connect4 AI

## Overview
The Connect4 AI is designed to play against a human player. It uses minimax algorithm with alpha-beta pruning to try and achieve the best possible move within a time limit.

## Time and space complexity

### Time complexity
The time complexity of the Connect4 AI is O(b^d) (where b is the number of possible moves per turn and d is the search depth).
This is due to iterative deepening approach, which evaluates all possible moves up to a given depth.

### Space complexity
The space complexity of the Connect4 AI is O(d) (where d is the search depth).
This is due to the recursion stack used in evaluation.

## Further fixes and improvements

### User interface
Currently there is no user interface for playing against the Connect4 AI, but it must be done through the command line instead. Adding an UI would make the gameplay more convenient and accessible for users.
If an UI was to be made, using bright colors on the player marker would make them easier to tell apart.

### AI strategy enhancements
There are also some improvements that could be made to the AI itself, like atrategizing to make a safe win instead of going for the closest win (which will probably be blocked by the opponent).

## Use of large language models
I used ChatGPT as a help to figure out different problems I was having, mostly by asking questions and conversing about different ways to solve the problems.