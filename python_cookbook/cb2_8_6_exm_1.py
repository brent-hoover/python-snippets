data = ["1", "2", 3, "4"]     # Typo: we 'forget' the quotes on data[2]
def pad4(seq):
    """
    Pad each string in seq with zeros up to four places. Note that there
    is no reason to actually write this function; Python already
    does this sort of thing much better.  It's just an example!
    """
    return_value = []
    for thing in seq:
        return_value.append("0" * (4 - len(thing)) + thing)
    return return_value
