from turtle import Turtle
FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.print_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        # print(f"{self.write('SCORE')}: {self.score}")
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align=ALIGNMENT, font=FONT)
