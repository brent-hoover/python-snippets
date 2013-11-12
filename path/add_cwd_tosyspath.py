#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


def main():
    sys.path.insert(0, os.path.abspath("."))

if __name__ == '__main__':
    print(sys.path)
    main()
    print(sys.path)
