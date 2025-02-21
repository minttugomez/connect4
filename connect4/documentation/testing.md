# Testing document
In this application, the testing is conducted using different testing strategies: unit testing, integration testing and user acceptance testing.

## Unit testing - Connect4

### Test case 1: Playing Turn
- Ensure no turn is played when the player index is invalid
- Ensure no turn is played when chosen column is full
- Ensure no turn is played when the input is invalid
- Verify that turn is played when the player and input are valid

### Test case 2: Switching turns
- Ensure the turn does not switch when the player index is invalid (raises a ValueError)
- Verify that after player 1 has made a successful move, turn is given to player 2
- Verify that after player 2 has made a successful move, turn is given to player 1

### Test case 3: Checking win
- Ensure a win is identified in horizontal direction
- Ensure a win is identified in vertical direction
- Ensure wins are identified in both diagonal directions
- Verify that no win is identified when there are no 4-in-a-rows

### Test case 4: Full grid
- Ensure full grid is correctly identified
- Verify that a grid is not identified as full when it still has open spots

### Test case 5: Reset grid
- Verify that the grid is successfully reset using the reset_grid method

## Unit testing - AI

### Test case 6: AI initialization
- Ensure columns, last cell, time limit, best moves and start time are initialized correctly

### Test case 7: AI playing turn
- Ensure AI is able to choose a column correctly
- Verify AI is able do the following:
    - choose a winning move
    - block opponent's win
    - choose a move that leads to a certain win in 5 moves

### Test case 8: Grid evaluation
- Ensure both AI and player wins are identified correctly

## Integration testing
- Verify that playing a turn works as intended
- Test invalid input works as intended in the case of:
    - column index out of range
    - column already full
    - grid completely full
- Ensure playing a winning move works as intended
- Verify that a filled grid without a win works as intended
- Verify that exiting the game works as intended
- Ensure that starting a new game works as intended

## User acceptance testing
I have conducted a lot of hands-on testing by playing Connect4 against the AI and trying to win. In the beginning this helped identify some flaws of the AI, but later on, the AI started winning every time, which I identified as a success.