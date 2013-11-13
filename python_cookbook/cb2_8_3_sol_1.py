import gc
def dump_garbage():
    """ show us what the garbage is about """
    # Force collection
    print "\nGARBAGE:"
    gc.collect()
    print "\nGARBAGE OBJECTS:"
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:77]+'...'
        print type(x),"\n  ", s
if __name__=="__main__":
    gc.enable()
    gc.set_debug(gc.DEBUG_LEAK)
    # Simulate a leak (a list referring to itself) and show it
    l = []
    l.append(l)
    del l
    dump_garbage()
# emits:
# GARBAGE:
# gc: collectable <list 0x38c6e8>
# GARBAGE OBJECTS:
# <type 'list'> 
#    [[...]]
