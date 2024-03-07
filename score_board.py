from turtle import Turtle
ALIGNMENT = "center"
FONT = ("align", 24, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()                       # hide the turtle
        self.updete_score()                     # call below function

    def updete_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updete_score()                     # call below function