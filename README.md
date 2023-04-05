# Nokia-Snake-Game-with-AI
 ![Working Demo](https://github.com/fola789/Nokia-Snake-Game-with-AI/blob/main/demo.png)

Current Status: Created working snake game where the snake is controlled by the user and the snake 

## Part 1 ~ Base Snake Game

- Step 1: Create display width and height ✔️
- Step 2: Set block size ✔️
- Step 3: Set available colours ✔️
- Step 4: Define an Enum to represent the possible directions the snake can move. ✔️
- Step 5: Define a namedtuple to represent a point in the game. ✔️
- Step 6: Initialize the class variables, including the display, clock, direction, head, snake, score, and food. ✔️
- Step 7: Define a method to place the food on the screen. ✔️
- Step 8: Define a play_step method to handle the main gameplay loop. ✔️
- Step 9 :Collect user input, including checking for keyboard events to change the direction of the snake. ✔️
- Step 10: Move the snake based on its current direction. ✔️
- Step 11: Check if the snake has collided with itself or the screen boundary. ✔️
- Step 12: Place new food if the snake has eaten the current food, otherwise move the existing food. ✔️
- Step 13: Update the user interface, including drawing the snake, food, and score. ✔️
- Step 14: Return whether the game is over and the current score. ✔️
- Step 15: Define a main method to create a SnakeGame object and run the game loop until the game is over. ✔️

## Part 2 ~ Fun additions
- Step 1: Create a flag to determine if the snake has gone out of the display boundary ✔️
- Step 2: If position is outside display boundary, update the position so  snake appears on the opposite side of the display ✔️
- Step 3: load image to the size of a block to act as food ✔️
- Step 4: Update functions ```_place_food(self):```, ```_update_ui(self):```✔️


## Part 3 ~ Pytest
Why Pytest? <br>

Pytest allows you to write concise tests that are easy to follow, easy to trace, provides excellent error reporting,
- Setup Pytest to test functions within our Pygame ✔️
- Test our ```_place_food(self):``` function to see if food has been placed within the board ✔️
- Test ```snake_pos``` and ```_place_food(self):``` to see if food has been eaten ✔️   


## Part 4 ~ AI
- Part 1: Implement the agent that controls the game.
- Part 2: Implement the neural network to predict the moves and train it.