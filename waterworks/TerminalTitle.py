"""Lets you change the title of your terminal in *NIX."""
import sys

template = "\033]0;%s\007"

def change_title(s):
    """Change the title of your terminal."""
    sys.stdout.write(template % s)
