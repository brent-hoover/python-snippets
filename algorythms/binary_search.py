#!/usr/bin/env python
# -*- coding: utf-8 -*-
__name__ = 'Binary Search'
__category__ = 'algorythms'
__type__ = 'example'


def search(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) / 2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    x = input('What is the number?')
    nums = range(1,101)
    print('Element is at index:%s' % search(x, nums))
    
if __name__ == '__main__':
    main()