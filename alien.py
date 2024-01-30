import turtle
import random


class Alien(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        turtle.register_shape("images/alien.gif")
        self.shape("images/alien.gif")
        self.penup()
        self.goto(x, y)
        self.speed = 1

    def move(self):
        x = self.xcor()
        x += self.speed
        self.setx(x)

        if x > 350 or x < -350:
            self.speed *= -1


class AlienArmy:
    def __init__(self, num_rows, aliens_per_row):
        self.num_rows = num_rows
        self.aliens_per_row = aliens_per_row
        self.aliens = []

    def create_army(self):
        for row in range(self.num_rows):
            num_aliens = self.aliens_per_row
            spacing = 700 / (num_aliens + 1)  # Calculate the spacing between aliens
            for i in range(num_aliens):
                x = -350 + (i + 1) * spacing  # Adjust the x-coordinate based on the index and spacing
                y = 250 - row * 30
                alien = Alien(x, y)
                self.aliens.append(alien)
                # print("Created alien at x =", x, "and y =", y)

    def move_army(self):
        for alien in self.aliens:
            alien.move()


class FireProjectile(turtle.Turtle):
    def __init__(self, player):
        super().__init__()
        turtle.register_shape("images/bullet.gif")
        self.shape("images/bullet.gif")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(player.xcor(), player.ycor() - 1)
        self.speed = 1

    def move(self):
        new_y = self.ycor()
        new_y -= self.speed
        self.goto(self.xcor(), new_y)

