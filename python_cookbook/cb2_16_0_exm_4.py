edge('A', 'B')
if 'X' in nodes:
    edge('X', 'A')
def triangle(n1, n2, n3):
    edge(n1, n2)
    edge(n2, n3)
    edge(n3, n1)
triangle('A','W','K')
execfile('mygraph.txt')     # Read graph from a datafile
