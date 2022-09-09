from turtle import Turtle
#
class Scoreboard(Turtle):
    #
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 230)
        self.write("Score: ", True, align="center", font=("Arial", 12))
    #
    def update_scoreboard(self, score):
        self.clear()
        self.setposition(0, 230)
        self.write(f"Score: {score}", True, align="center", font=("Arial", 12))
    #
    def print_final_score(self, score):
        self.clear()
        self.setposition(0, 0)
        message = f"Game Over.\nYour Score: {score}"
        self.write(message, True, align="center", font=("Arial", 12))
