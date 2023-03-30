import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2 
    UP  = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
class SnakeGame:
    # Initialize the game with a specified width and height
    def __init__(self, w=640, h=480):
        # Set width and height
        self.w = w
        self.h = h
        
        # Initialize the display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake') # Set window title
        self.clock = pygame.time.Clock() # Initialize the clock

        # initialize the game state
        self.direction = Direction.RIGHT # Set the starting direction
        
        # Initialize the snake with a head and two tail pieces
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0 # Initialize the score to 0
        self.food = None # Set food to None until it is placed
        self._place_food() # Place the first food
    
    # Place a new food on the game board    
    def _place_food(self):
        # Generate random coordinates for the food within the game board
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE
        
        # Create a new Point object with the generated coordinates
        self.food = Point(x, y)
        
        # Create a new Point object with the generated coordinates
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. collect user input
        
        # 2. Move the snake
        
        # 3. Check if game over
        
        # 4. Place new food or just move
        
        # 5. Update ui and clock
        
        # 6. Return game over and score
        game_over = False # Initialize game over flag to False
        return game_over, self.score # Return the game over flag and current score
        pass
        
if __name__ == '__main__':
    game = SnakeGame()
        
    # Game loop
    while True:
        game_over, score = game.play_step() # Perform one step of the game and get the game over flag and score
        
        if game_over == True: # If the game is over, break out of the loop
            break
        
    print('Final Score', score ) # Print the final score
            
        # Break if game over
            
    pygame.quit() # Quit pygame when the game is over
    
    