#!/usr/bin/python
 
import sys
from socket import *
 
for port in range(int(sys.argv[2].split(''-'')[0]), int(sys.argv[2].split(''-'')[1])+1):
    try:socket(AF_INET, SOCK_STREAM).connect((sys.argv[1], port)); print "Able to connect to port:", port
    except: 
        pass
