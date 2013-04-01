"""Not actually from the Python Cookbook, but useful nonetheless.

Lifted from http://pdos.csail.mit.edu/~cblake/cls/cls.py
"""

import os

def ioctl_GWINSZ(fd):
    try:
        import fcntl, termios, struct
        cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        return None
    return cr

def terminal_size(default=(25, 80)):
    """Will return *some* terminal size.  If no terminal size can be
    determined, returns the defauult."""
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)  # try open fds
    if not cr:                                                  # ...then ctty
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:                            # env vars or finally defaults
        try:
            env = os.environ
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])         # reverse rows, cols
