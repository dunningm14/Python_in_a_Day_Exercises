# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose:  The Tech Academy Python Course, Step 16/63
#           The exercise 3-4 that prints 'spam' a specified
#           number of times
#


def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print ''
