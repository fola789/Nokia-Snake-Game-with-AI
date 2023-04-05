import pytest
from snake_game import BLOCK_SIZE, Point, SnakeGame

def test_place_food():
    snake = SnakeGame()
    snake._place_food(*snake.generate_food())
    
    # Check if the food is a Point object
    assert isinstance(snake.food, Point)
    
    # Check if the food is within the game board
    assert 0 <= snake.food.x < snake.w
    assert 0 <= snake.food.y < snake.h
    
    # Check if the food does not overlap with the snake
    assert snake.food not in snake.snake

def test_eats_food():
    snake_game = SnakeGame()
    snake_pos = snake_game.snake[1]
    snake_game._place_food(snake_pos.x + BLOCK_SIZE, snake_pos.y + BLOCK_SIZE)
    print(snake_game.food, snake_game.snake)
    assert snake_game.food in snake_game.snake
   
   
test_place_food()
test_eats_food()