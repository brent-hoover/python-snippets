#!/usr/bin/env python
#coding:utf-8

def reverse(s):
    print('s is:%s' % s)
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]

def anagrams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

def main():
    to_reverse = raw_input('Anagram what string? ')
    print(to_reverse)
    print(anagrams(to_reverse))

if __name__ == '__main__':
    main()