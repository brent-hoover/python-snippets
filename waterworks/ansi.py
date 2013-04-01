#!/usr/bin/env python 
'''
ansi.py

ANSI Terminal Interface

(C)opyright 2000 Jason Petrone <jp_py@demonseed.net>
All Rights Reserved

Color Usage:
  print RED + 'this is red' + RESET
  print BOLD + GREEN + WHITEBG + 'this is bold green on white' + RESET

Commands:
  def move(new_x, new_y): 'Move cursor to new_x, new_y'
  def moveUp(lines): 'Move cursor up # of lines'
  def moveDown(lines): 'Move cursor down # of lines'
  def moveForward(chars): 'Move cursor forward # of chars'
  def moveBack(chars): 'Move cursor backward # of chars'
  def save(): 'Saves cursor position'
  def restore(): 'Restores cursor position'
  def clear(): 'Clears screen and homes cursor'
  def clrtoeol(): 'Clears screen to end of line'
'''

################################
# C O L O R  C O N S T A N T S #
################################
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

RESET = '\033[0;0m'
BOLD = '\033[1m'
REVERSE = '\033[2m'

BLACKBG = '\033[40m'
REDBG = '\033[41m'
GREENBG = '\033[42m'
YELLOWBG = '\033[43m'
BLUEBG = '\033[44m'
MAGENTABG = '\033[45m'
CYANBG = '\033[46m'
WHITEBG = '\033[47m'

def move(new_x, new_y):
  'Move cursor to new_x, new_y'
  print '\033[' + str(new_x) + ';' + str(new_y) + 'H'

def moveUp(lines):
  'Move cursor up # of lines'
  print '\033[' + str(lines) + 'A'

def moveDown(lines):
  'Move cursor down # of lines'
  print '\033[' + str(lines) + 'B'

def moveForward(chars):
  'Move cursor forward # of chars'
  print '\033[' + str(lines) + 'C'

def moveBack(chars):
  'Move cursor backward # of chars'
  print '\033[' + str(lines) + 'D'

def save():
  'Saves cursor position'
  print '\033[s'

def restore():
  'Restores cursor position'
  print '\033[u'

def clear():
  'Clears screen and homes cursor'
  print '\033[2J'

def clrtoeol():
  'Clears screen to end of line'
  print '\033[K'
