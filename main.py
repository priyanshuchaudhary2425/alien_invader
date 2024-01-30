import turtle
import math
from spaceinvador import Player, FireBullet
from alien import AlienArmy, FireProjectile
import random

# SET UP WINDOW

window = turtle.Screen()
window.bgpic('images/space-bg.png')
window.setup(width=800, height=600)
window.title("Space Invaders")
window.tracer(0)

# INITIATING FUNCTIONS
player = Player()
bullets = []  # Store the bullets in a list
alien_bullets = []

alien_army = AlienArmy(num_rows=4, aliens_per_row=14)
alien_army.create_army()

window.listen()
window.onkeypress(player.move_left, "Left")
window.onkeypress(player.move_right, "Right")


def shoot_bullet():
    if len(bullets) < 3:
        bullet = FireBullet(player)
        bullets.append(bullet)
        window.onkey(shoot_bullet, "space")


def check_collision(bullet, target):
    distance = math.sqrt(
        math.pow(bullet.xcor() - target.xcor(), 2) + math.pow(bullet.ycor() - target.ycor(), 2))
    return distance < 15  # Adjust the collision threshold as needed


def game_loop():
    game_over = False

    while not game_over:
        alien_army.move_army()

        aliens_to_fire = random.sample(alien_army.aliens, random.randint(1, 3))

        for alien in aliens_to_fire:
            if random.randint(1, 1000) <= 2:
                attack = FireProjectile(alien)
                alien_bullets.append(attack)

        for alien_bullet in alien_bullets:
            alien_bullet.move()
            if alien_bullet.ycor() < -400:
                alien_bullets.remove(alien_bullet)

            if check_collision(alien_bullet, player):
                print("Player ship hit by alien bullet!")
                game_over = True
                break

        # Move and update bullets
        for bullet in bullets:
            bullet.fire_bullet()
            if bullet.ycor() > 400:
                bullets.remove(bullet)

            for alien in alien_army.aliens:
                if check_collision(bullet, alien):
                    bullet.hideturtle()  # Hide the bullet
                    alien.goto(1000, 1000)  # Move the collided alien off the screen
                    bullets.remove(bullet)  # Remove the bullet from the list
                    break  # Exit the loop if a collision is detected

        window.update()

    game_over_text = turtle.Turtle()
    game_over_text.color("white")
    game_over_text.penup()
    game_over_text.goto(0, 0)
    game_over_text.write("Game Over", align="center", font=("Courier", 24, "normal"))
    game_over_text.hideturtle()


window.onkey(shoot_bullet, "space")  # Register the spacebar event to fire the first bullet
game_loop()

window.mainloop()
