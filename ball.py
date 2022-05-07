from turtle import Turtle


class Ball(Turtle):
    x_cord: int
    y_cord: int
    move_speed: int

    def __init__(self) -> None:
        super().__init__("circle")
        self.pu()
        self.color("purple")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_cord = 10
        self.y_cord = 10
        self.move_speed = 0.2
        self.go_towards_right()

    def move(self) -> None:
        new_x_cord = self.xcor() + self.x_cord
        new_y_cord = self.ycor() + self.y_cord
        self.goto(new_x_cord, new_y_cord)

    def get_y(self) -> float:
        return self.ycor()

    def get_x(self) -> float:
        return self.xcor()

    def bounce(self) -> None:
        self.y_cord *= -1

    def bounce_paddle(self) -> None:
        self.x_cord *= -1
        self.move_speed *= 0.9

    def reset_position(self) -> None:
        self.clear()
        self.goto(0, 0)

    def go_towards_left(self) -> None:
        self.x_cord = -10
        self.y_cord = 10

    def go_towards_right(self) -> None:
        self.x_cord = 10
        self.y_cord = 10
