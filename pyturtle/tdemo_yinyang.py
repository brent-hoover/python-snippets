#!/usr/bin/env python
#
# [SNIPPET_NAME: Yin Yang]
# [SNIPPET_CATEGORIES: PyTurtle]
# [SNIPPET_DESCRIPTION: Use turtle to draw a yin yang.]
# [SNIPPET_DOCS: http://docs.python.org/library/turtle.html]
# [SNIPPET_AUTHOR: Grant Bowman <grantbow@ubuntu.com>]
# [SNIPPET_LICENSE: PSF]
# Code authorship from http://python.org/download/releases/2.6.4/


"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("black")
    fill(True)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    color(color1)
    fill(True)
    color(color2)
    left(90)
    up()
    forward(radius*0.375)
    right(90)
    down()
    circle(radius*0.125)
    left(90)
    fill(False)
    up()
    backward(radius*0.375)
    down()
    left(90)

def main():
    reset()
    yin(200, "white", "black")
    yin(200, "black", "white")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
