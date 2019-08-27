"""
Bounce a ball on the screen, using gravity.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_ball
"""

import arcade
from vector import *

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Ball Example"

# Size of the circle.
CIRCLE_RADIUS = 20

# How strong the gravity is.
GRAVITY_CONSTANT = 1.2

# Length of pendulum
PENDULUM_LENGTH = SCREEN_WIDTH/4

# Percent of velocity maintained on a bounce.
BOUNCINESS = 0.6



def draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """
    dt = delta_time*1

    # Start the render. This must happen before any drawing
    # commands. We do NOT need an stop render command.
    arcade.start_render()

    # Draw our object
    arcade.draw_circle_filled(draw.pos.x, draw.pos.y, CIRCLE_RADIUS, arcade.color.BLACK)
    # Draw the rigid pendulum
    arcade.draw_line(draw.origo.x, draw.origo.y, draw.pos.x, draw.pos.y, arcade.color.BLACK, 3)

    # New positon
    new_pos = Vector2d(0, 0)
    new_pos.x = draw.pos.x + draw.vel.x*dt + draw.acc.x*(dt*dt*0.5)
    new_pos.y = draw.pos.y + draw.vel.y*dt + draw.acc.y*(dt*dt*0.5)

    # Apply forces
    force_g = Vector2d(0, -9.82*100)
    origo = Vector2d(draw.origo.x, draw.origo.y)
    ball = Vector2d(draw.pos.x, draw.pos.y)
    s = Sub(draw.origo, ball)
    force_s = s.Mul( -Dot(force_g, s)/s.SqrLength() )  
    force = Add(force_s, force_g)

    arcade.draw_line(draw.pos.x, draw.pos.y, draw.pos.x + force.x*0.1, draw.pos.y + force.y*0.1, arcade.color.BLUE, 1)
    arcade.draw_line(draw.pos.x, draw.pos.y, draw.pos.x + force_g.x*0.1, draw.pos.y + force_g.y*0.1, arcade.color.RED, 1)
    if force_s.SqrLength() > 0.000001:
        arcade.draw_line(draw.pos.x, draw.pos.y, draw.pos.x + force_s.x*0.1, draw.pos.y + force_s.y*0.1, arcade.color.RED, 1)

    if draw.vel.SqrLength() > 0.000001:
        arcade.draw_line(draw.pos.x, draw.pos.y, draw.pos.x + draw.vel.x*0.1, draw.pos.y + draw.vel.y*0.1, arcade.color.ORANGE, 1)

    new_acc = Vector2d( force.x, force.y )

    # New velocity
    new_vel = Vector2d(0,0);
    new_vel.x = draw.vel.x + (draw.acc.x + new_acc.x)*(dt*0.5)
    new_vel.y = draw.vel.y + (draw.acc.y + new_acc.y)*(dt*0.5)

    draw.pos.x = new_pos.x
    draw.pos.y = new_pos.y
    draw.vel.x = new_vel.x
    draw.vel.y = new_vel.y
    draw.acc.x = new_acc.x
    draw.acc.y = new_acc.y

    # Align velocity with force
    velocity_mag = draw.vel.Length()
    force_mag = draw.acc.Length()
#    friction = 0.99952
    friction = 1.001
    if force_mag > 0.000001:
        if Dot(draw.vel, draw.acc) >= 0:
            draw.vel.x = friction*draw.acc.x*velocity_mag/force_mag
            draw.vel.y = friction*draw.acc.y*velocity_mag/force_mag
        else:
            draw.vel.x = -friction*draw.acc.x*velocity_mag/force_mag
            draw.vel.y = -friction*draw.acc.y*velocity_mag/force_mag

    # The forces may have bent the string, keep the pendulum rigid by adjusting position
    ball = Vector2d(draw.pos.x,draw.pos.y)
    n = Sub(ball, origo).Normalize()
    draw.pos.x = origo.x + n.x*PENDULUM_LENGTH
    draw.pos.y = origo.y + n.y*PENDULUM_LENGTH

# Below are function-specific variables. Before we use them
# in our function, we need to give them initial values. Then
# the values will persist between function calls.
#
# In other languages, we'd declare the variables as 'static' inside the
# function to get that same functionality.
#
# Later on, we'll use 'classes' to track position and velocity for multiple
# objects.
draw.pos = Vector2d(SCREEN_WIDTH/2 - PENDULUM_LENGTH, SCREEN_HEIGHT/2)
draw.vel = Vector2d(0, 0)
draw.acc = Vector2d(0, 0)
#draw.x = SCREEN_HEIGHT/2 - PENDULUM_LENGTH
#draw.y = SCREEN_HEIGHT/2
#draw.delta_x = 0
#draw.delta_y = 0
draw.origo = Vector2d(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
#draw.origo_x = SCREEN_WIDTH/2
#draw.origo_y = SCREEN_HEIGHT/2

def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(draw, 1 / 80)

    # Run the program
    arcade.run()

    # When done running the program, close the window.
    arcade.close_window()


if __name__ == "__main__":
    main()
