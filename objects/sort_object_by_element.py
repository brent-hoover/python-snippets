import operator

class Thing(object):
    
    def __init__(self, num):
        self.num = num
        
    def __repr__(self):
        return str(self.num)

def nonesorter(a):
    if a.num is None:
        return ""
    return a.num
        
thing_list = list()
for x in range(10, 0, -1):
    thing_list.append(Thing(x))
thing_list.append(Thing(None))

print(thing_list)

sorted_things = sorted(thing_list, key=nonesorter)
print(sorted_things)