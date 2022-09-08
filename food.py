from turtle import Turtle
import random
#
class Food(Turtle):
    #
    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("circle")
        self.color("red")
        self.radius = 12
        self.set_random_position(width, height)   
    #
    def genrate_random_position(self, width, height):
        offset = 20
        x_random_position = random.randint(- width / 2 + offset, width / 2 - offset)
        y_random_position = random.randint(- height / 2 + offset, height / 2 - offset)
        return x_random_position, y_random_position
    #
    def set_random_position(self, width, height):
        x_food_pos, y_food_pos = self.genrate_random_position(width, height)
        self.setposition(x_food_pos, y_food_pos)
        self.showturtle()