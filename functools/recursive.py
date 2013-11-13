#!/usr/bin/env python
#coding:utf-8

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def main():
    find_factorial = input('Find the Factorial for what number? ')
    print(fact(find_factorial))

if __name__ == '__main__':
    main()
