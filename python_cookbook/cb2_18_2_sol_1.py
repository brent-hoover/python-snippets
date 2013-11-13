# support 2.3 as well as 2.4
try: set
except NameError: from sets import Set as set
# f defines an equivalence relation among items of sequence seq, and
# f(x) must be hashable for each item x of seq
def uniquer(seq, f=None):
    """ Keeps earliest occurring item of each f-defined equivalence class """
    if f is None:    # f's default is the identity function f(x) -> x
        def f(x): return x
    already_seen = set()
    result = []
    for item in seq:
        marker = f(item)
        if marker not in already_seen:
             already_seen.add(marker)
             result.append(item)
    return result
