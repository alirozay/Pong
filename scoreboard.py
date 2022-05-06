from turtle import Turtle
FINAL_SCORE = 3

class ScoreBoard(Turtle):
    right_score: int
    left_score: int

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.goto(-100, 270)
        self.display_score()

    def display_score(self) -> None:
        self.goto(-100, 250)
        self.write(self.left_score, move=False, align='center',
                   font=("Courier", 30, "normal"))
        self.goto(100, 250)
        self.write(self.right_score, move=False, align='center',
                   font=("Courier", 30, "normal"))

    def left_score_update(self) -> None:
        self.left_score += 1
        self.clear()
        self.display_score()

    def right_score_update(self) -> None:
        self.clear()
        self.right_score += 1
        self.display_score()

    def game_over(self) -> bool:
        if self.left_score == FINAL_SCORE:
            self.clear()
            self.goto(0,0)
            self.write("Left player wins", move=False, align='center',
                       font=("Courier", 30, "normal"))
            self.goto(0, 100)
            self.write(f"{self.left_score} vs {self.right_score}", move=False, align='center',
                       font=("Courier", 30, "normal"))
            return True
        elif self.right_score == FINAL_SCORE:
            self.clear()
            self.goto(0,0)
            self.write("Right player wins", move=False, align='center',
                       font=("Courier", 30, "normal"))
            self.goto(0, 100)
            self.write(f"{self.left_score} vs {self.right_score}", move=False, align='center',
                       font=("Courier", 30, "normal"))
            return True
        return False

