nodes = {}
def getnode(name):
    " Return the node with the given name, creating it if necessary. "
    if name in nodes:
        node = nodes[name]
    else:
        node = nodes[name] = node(name)
    return node
class node(object):
     " A node has a name and a list of edges emanating from it. "
    def __init__(self, name):
        self.name = name
        self.edgelist = []
class edge(object):
    " An edge connects two nodes. "
    def __init__(self, name1, name2):
        self.nodes = getnode(name1), getnode(name2)
        for n in self.nodes:
            n.edgelist.append(self)
    def __repr__(self):
        return self.nodes[0].name + self.nodes[1].name
