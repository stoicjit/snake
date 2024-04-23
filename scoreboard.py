from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
           self.highscore = int(data.read())
        self.penup()
        self.speed('fastest')
        self.goto(0, 260)
        self.color('white')
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', align='center', font=('Arial', 15, 'normal'))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()