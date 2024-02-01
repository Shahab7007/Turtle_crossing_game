from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("black")
        self.goto(-245, 270)
        self.level_update()

    def level_update(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

