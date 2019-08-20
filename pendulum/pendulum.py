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

    # Start the render. This must happen before any drawing
    # commands. We do NOT need an stop render command.
    arcade.start_render()

    # Draw our rectangle
    arcade.draw_circle_filled(draw.x, draw.y, CIRCLE_RADIUS,
                              arcade.color.BLACK)

    arcade.draw_line(draw.origo_x, draw.origo_y, draw.x, draw.y, arcade.color.BLACK, 3)

    # Test swinging pendulum
    force_g = Vector2d(0, -9.82*100)
    origo = Vector2d(draw.origo_x, draw.origo_y)
    ball = Vector2d(draw.x,draw.y)
    s = Sub(origo, ball)
    force_s = s.Mul( -Dot(force_g, s)/s.SqrLength() )  
    force = Add(force_s, force_g)

    draw.delta_x += force.x*delta_time
    draw.delta_y += force.y*delta_time

    # Modify rectangles position based on the delta
    # vector. (Delta means change. You can also think
    # of this as our speed and direction.)
    draw.x += draw.delta_x*delta_time
    draw.y += draw.delta_y*delta_time

    # The forces may have bent the string, keep the pendulum rigid by adjusting position
    ball = Vector2d(draw.x,draw.y)
    n = Sub(ball, origo).Normalize()
    draw.x = origo.x + n.x*PENDULUM_LENGTH
    draw.y = origo.y + n.y*PENDULUM_LENGTH


# Below are function-specific variables. Before we use them
# in our function, we need to give them initial values. Then
# the values will persist between function calls.
#
# In other languages, we'd declare the variables as 'static' inside the
# function to get that same functionality.
#
# Later on, we'll use 'classes' to track position and velocity for multiple
# objects.
draw.x = SCREEN_HEIGHT/2 - PENDULUM_LENGTH
draw.y = SCREEN_HEIGHT/2
draw.delta_x = 0
draw.delta_y = 0
draw.origo_x = SCREEN_WIDTH/2
draw.origo_y = SCREEN_HEIGHT/2


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
