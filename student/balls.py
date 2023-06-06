'''
A game made with pygame zero where u click on the screen and balls of random color will spawn in. The balls will all be of different color, shape size and speed.
'''
import random
import pgzrun
import math

WIDTH = 800
HEIGHT = 600

balls = []


# Function to handle mouse clicks
def on_mouse_down(pos, button):
    # Check if button is pressed
    if :
         # Get the position where the mouse was clicked
        x = pos[0]
        y = pos[1]
        # Generate random attributes for the ball for radius use and random use randint and for angle use uniform(00,2* math.pi) also for dx,dy use sin and cos resp
        radius = 
        speed = 
        angle = 
        dx = speed * 
        dy = speed * 
        
        #Generate a random color for the ball using RGB values
        
        # append as all the variables as a tuple to balls

# Function to update the game state
def update():
    for i in range(len(balls)):
        # use tuple unpacking to get the variables for all the balls
        x, y, radius, color, dx, dy = balls[i]
         # Update the position of the ball based on its speed and direction
       
        # Check for collisions with the screen boundaries and reflect the ball's direction
        if x - radius < 0 or x + radius > WIDTH:
            dx = -dx
        if y - radius < 0 or y + radius > HEIGHT:
            dy = -dy
        balls[i] = (x, y, radius, color, dx, dy)
# Function to draw the game objects on the screen
def draw():
    screen.clear()
    for x, y, radius, color, _, _ in balls:
        # Draw a filled circle representing each ball
        screen.draw.filled_circle((x, y), radius, color)

pgzrun.go()
