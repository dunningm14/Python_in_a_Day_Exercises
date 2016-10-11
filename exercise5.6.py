# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Chapter 5, exercise 6
# 1. Write a function called koch that takes a turtle and a length as parameters,
# and that uses the turtle to draw a Koch curve with the given length.
# 2. Write a function called snowflake that draws three Koch curves to make
# the outline of a snowflake.


from TurtleWorld import *

def koch ( t, length ) :
    if length > 3 :
        l_o_3 = length / 3.0
        koch (t, l_o_3 )
        lt(t, 60 )
        koch (t, l_o_3 )
        rt(t, 120)
        koch ( t, l_o_3 )
        lt(t, 60)
        koch ( t, l_o_3 )
    else :
        fd( t, length )

def snowflake ( t, length ) :
    t.set_pen_color('green')
    for i in range(3) :
        koch ( t, length )
        rt (t, 120 )
