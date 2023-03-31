import pygame
import random
from enum import Enum
from collections import namedtuple

# Personal Notes
#  self is a reference to the current instance of the class.
#  It is used as the first parameter in instance methods to refer to the instance variables and methods of the current object.
#  self is used to refer to the instance of the SnakeGame class and its attributes such as self.w, self.h, self.direction, self.head, 
#  self.snake, self.score, and self.food. These attributes are defined and initialized within the __init__ method, and can be accessed 
#  and modified by any instance method using the self parameter.
pygame.init()
font = pygame.font.Font('arial/arial.ttf', 25) # faster run time 
#font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2 
    UP  = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 15

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.direction = Direction.RIGHT
                    elif event.key == pygame.K_UP:
                        self.direction = Direction.UP
                    if event.key == pygame.K_DOWN:
                        self.direction = Direction.DOWN              
                
        # 2. Move the snake
        self._move(self.direction)
        self.snake.insert(0, self.head)
        
        # 3. Check if game over
        game_over = False
        if self._is_collision():
                game_over = True
                return game_over, self.score
            
        # 4. Place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop() 
             
        # 5. Update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        
        # 6. Return game over and score
        return game_over, self.score 
    
    # Method to detect collision    
    def _is_collision(self):
        #hits boundary
        if self.head.x > self.w - BLOCK_SIZE:
            self.head.x = 0
        elif self.head.x < 0:
            self.head.x = self.w - BLOCK_SIZE
        elif self.head.y > self.h - BLOCK_SIZE:
            self.head.y = 0
        elif self.head.y < 0:
            self.head.y = self.h - BLOCK_SIZE
        
        # hits itself
        if self.head in self.snake[1:]:
                return True
        
        return False
    
    # Method to update UI to reflect the current game state.    
    def _update_ui(self):
        # Fills the display with a black color to clear the previous state of the game.
        self.display.fill(BLACK)
        
        # Draw the snake
        for pt in self.snake:
                pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12)) # second slightly smaller rectangle to create 3d effecct 
                
        # Draw the food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE )) 
        
        # Draws the current score
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        
        # update the entire display with the new state of the game.
        pygame.display.flip()
    
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
            if x > self.w - BLOCK_SIZE:
                x = 0
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
            if x < 0:
                x = self.w - BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
            if y > self.h - BLOCK_SIZE:
                y = 0
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            if y < 0:
                y = self.h - BLOCK_SIZE
            
        self.head = Point(x, y)
    
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
    
    