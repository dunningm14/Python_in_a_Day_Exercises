# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose: Chapter 5, exercise 5
# The function draws a tree 
# and then the Turtle ends up back where he started.

def draw(t, length, n):
 if n == 0:
     return
     angle = 50
     fd(t, length*n)
     lt(t, angle)
     draw(t, length, n-1)
     rt(t, 2*angle)
     draw(t, length, n-1)
     lt(t, angle)
     bk(t, length*n)
 
