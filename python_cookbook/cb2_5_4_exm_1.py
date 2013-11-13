def _sorted_keys(container, keys, reverse):
    ''' return list of 'keys' sorted by corresponding values in 'container' '''
    aux = [ (container[k], k) for k in keys ]
    aux.sort()
    if reverse: aux.reverse()
    return [k for v, k in aux]
