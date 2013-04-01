#!/usr/bin/env python
# -*-mode: python; coding: iso-8859-1 -*-
#
# Copyright (c) Peter Astrand <astrand@cendio.se>

"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/439045
Title: Read a text file backwards (yet another implementation)
Submitter: Peter Astrand
Last Updated: 2005/08/11
Version no: 1.0
Category: Files

Description:
Yet another way to read a file line by line, starting at the end. 

Modified by dmcc: put __init__ at top, testing code in __main__ and
add __iter__ method.
"""

import os
import string

class BackwardsReader:
    """Read a file line by line, backwards"""
    BLKSIZE = 4096
    def __init__(self, file):
        self.file = file
        self.buf = ""
        self.file.seek(0, 2)
    def readline(self):
        while 1:
            newline_pos = string.rfind(self.buf, "\n")
            if newline_pos != -1:
                # Found a newline
                line = self.buf[newline_pos+1:]
                self.buf = self.buf[:newline_pos]
                return line + "\n"
            else:
                pos = self.file.tell()
                if pos == 0:
                    # Start-of-file
                    return ""
                else:
                    # Need to fill buffer
                    backseek = min(self.BLKSIZE, pos)
                    self.file.seek(-backseek, 1)
                    self.buf = self.file.read(self.BLKSIZE) + self.buf
                    self.file.seek(-backseek, 1)
                    if pos - backseek == 0:
                        self.buf = "\n" + self.buf
    def __iter__(self):
        while 1:
            line = self.readline()
            if line is "":
                break
            else:
                yield line

if __name__ == "__main__":
    # Example usage
    br = BackwardsReader(open('bar'))

    while 1:
        line = br.readline()
        if not line:
            break
        print repr(line)
