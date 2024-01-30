import turtle


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("images/player.gif")
        self.shape("images/player.gif")
        self.color("green")
        self.penup()
        self.goto(x=0, y=-250)

    def move_left(self):
        new_x = self.xcor() - 10
        if new_x > -375:  # LIMIT X-AXIS MOVEMENT T0 -300
            self.goto(x=new_x, y=self.ycor())

    def move_right(self):
        new_x = self.xcor() + 10
        if new_x < 375:  # LIMIT X-AXIS MOVEMENT TO 300
            self.goto(x=new_x, y=self.ycor())


class FireBullet(turtle.Turtle):
    def __init__(self, player):
        super().__init__()
        turtle.register_shape("images/bullet.gif")
        self.shape("images/bullet.gif")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(player.xcor(), player.ycor() + 10)
        self.speed = 3

    def fire_bullet(self):
        new_y = self.ycor()
        new_y += self.speed
        self.goto(self.xcor(), new_y)
