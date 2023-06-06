'''
A game made with pygame zero where u click on the screen and balls of random color will spawn in. The balls will all be of different color, shape size and speed.
'''
import random
import pgzrun
import math

WIDTH = 800
HEIGHT = 600

balls = []

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        x = pos[0]
        y = pos[1]
        radius = random.randint(10, 50)
        speed = random.randint(5, 10)
        angle = random.uniform(0, 2 * math.pi)
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        balls.append((x, y, radius, color, dx, dy))

def update():
    for i in range(len(balls)):
        x, y, radius, color, dx, dy = balls[i]
        x += dx
        y += dy
        if x - radius < 0 or x + radius > WIDTH:
            dx = -dx
        if y - radius < 0 or y + radius > HEIGHT:
            dy = -dy
        balls[i] = (x, y, radius, color, dx, dy)

def draw():
    screen.clear()
    for x, y, radius, color, _, _ in balls:
        screen.draw.filled_circle((x, y), radius, color)

pgzrun.go()
