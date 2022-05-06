from turtle import Turtle
from typing import Tuple

MOVEMENT = 20


class Paddle(Turtle):

    def __init__(self, coordinates: Tuple[int, int]):
        super().__init__("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def up(self) -> None:
        current_y = self.ycor()
        if current_y + MOVEMENT <= 240:
            current_y += MOVEMENT
            self.sety(current_y)

    def down(self) -> None:
        current_y = self.ycor()
        if current_y - MOVEMENT >= -240:
            current_y -= MOVEMENT
            self.sety(current_y)
