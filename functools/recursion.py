def sort( a ):
    if len(a) == 1: return a
    part1= sort( a[:len(a)//2] )
    part2= sort( a[len(a)//2:] )
    return merge( part1, part2 )

#Merge, defined recursively.

def merge( a, b ):
    if len(b) == 0: return a
    if len(a) == 0: return b
    if a[0] < b[0]:
        return [ a[0] ] + merge(a[1:], b)
    else:
        return [ b[0] ] + merge(a, b[1:]) 

#Linear search, defined recursively.

def find( element, sequence ):
    if len(sequence) == 0: return False
    if element == sequence[0]: return True
    return find( element, sequence[1:] )

#Binary search, defined recursively.

def binsearch( element, sequence ):
    if len(sequence) == 0: return False
    mid = len(sequence)//2
    if element < mid: 
        return binsearch( element, sequence[:mid] )
    else:
        return binsearch( element, sequence[mid:] )

