# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose:  The exercises from chapter 4


# importing swampy and the built-in math functions
import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


# exercise one that draws a square with a turtle. At the end it returns the turtle
# to the starting position
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob)


# Another parameter is added called 'length' to the square function. The length
# of the sides = 'length'
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
        
square(bob, 100)


# create a function called polygon that draws regular polygons with any number
# of sides
def polygon(t, n, length):
     angle = 360.0 / n
     for i in range(n):
         fd(t, length)
         lt(t, angle)

polygon(bob, 7, 70)



# Draws a polygon that takes an angle as a third argument
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


# Draws a polygon with n sides
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


# Draws an arc with a specific angle and radius
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n


# draws a circle with a particular radius
def circle(t, r):
    arc(t, r, 360)


# draws a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    wait_for_user()


# Checks whether we are running as a script,
# in which case run the test code, or being imported, in which
# case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

