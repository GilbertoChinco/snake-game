from turtle import Turtle
#
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_body()
    #
    def create_body(self):
        for position in self.starting_position:
            self.add_segment(position)
    #
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    #
    def extend_body(self):
        self.add_segment(self.segments[-1].position())
    #
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(new_x, new_y)
        self.segments[0].forward(20)
    #
    def direction_north(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    #
    def direction_south(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    #
    def direction_west(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    #
    def direction_east(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    #
    def is_position_out_of_bounds(self):
        x_position = self.segments[0].xcor()
        y_position = self.segments[0].ycor()
        if abs(x_position) > 250 or abs(y_position) > 250:
            return True
        return False
    #
    def is_collioned_with_food(self, food):
        snake_x_position = self.segments[0].xcor()
        snake_y_position = self.segments[0].ycor()
        food_x_position = food.xcor()
        food_y_position = food.ycor()
        # (x - h) ** 2 + (y - k) ** 2 <= r ** 2
        # (x, y): snake position
        # (h, k): food position
        x_part = (snake_x_position - food_x_position) ** 2
        y_part = (snake_y_position - food_y_position) ** 2
        radius = food.radius ** 2
        if x_part + y_part <= radius:
            self.extend_body()
            food.hideturtle()
            return True
        return False
    #
    def is_collioned_with_tail(self):
        head = self.segments[0]
        x_cor_head = head.xcor()
        y_cor_head = head.ycor()
        for i in range(1, len(self.segments)):
            x_cor_segment = self.segments[i].xcor()
            y_cor_segment = self.segments[i].ycor()

            if x_cor_head == x_cor_segment and y_cor_head == y_cor_segment:
                return True

        return False
