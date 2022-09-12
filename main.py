from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from configuration import setup
import time
#
#   Screen Configuration
#
score = 0
screen = Screen()
screen.tracer(0)    
screen.setup(setup["width"], setup["height"])
screen.bgcolor(setup["background-color"])
#
#   Create Objects
#
snake = Snake()
food = Food(setup["width"], setup["height"])
scoreboard = Scoreboard()
#
#   Add event listeners
#
screen.update()
screen.listen()
screen.onkey(fun=snake.direction_north, key="w")
screen.onkey(fun=snake.direction_south, key="s")
screen.onkey(fun=snake.direction_west, key="a")
screen.onkey(fun=snake.direction_east, key="d")
#
#   Main loop
#
is_game_over = False
#
while not is_game_over:
    screen.update()
    time.sleep(0.05)
    snake.move()
    #
    if snake.is_collioned_with_tail():
        scoreboard.print_final_score(score)
        is_game_over = True
        break
    #
    if snake.is_collioned_with_food(food):
        screen.update()
        score += 1
        food = Food(setup["width"], setup["height"])
        scoreboard.update_scoreboard(score)
        screen.update()
    #
    if snake.is_position_out_of_bounds():
        scoreboard.print_final_score(score)
        is_game_over = True
        break
#
screen.exitonclick()