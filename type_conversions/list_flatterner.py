#!/usr/bin/env python
# List flattener



def flatten_list(list_to_flatten):
    for i, f in enumerate(list_to_flatten):
        if hasattr(f, '__iter__'):
            del list_to_flatten[i]
            list_to_flatten[i:i] = f
    return list_to_flatten
    
 
if __name__ == '__main__':
    list_to_flatten = ['one', 'two', 'three', ['a', 'b', 'c'], 'four']
    print(flatten_list(list_to_flatten))
