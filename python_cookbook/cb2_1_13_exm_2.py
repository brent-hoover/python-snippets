def fields(baseformat, theline, lastfield=False, _cache={}):
    # build the key and try getting the cached format string
    key = baseformat, len(theline), lastfield
    format = _cache.get(key)
    if format is None:
        # no format string was cached, build and cache it
        numremain = len(theline)-struct.calcsize(baseformat)
        _cache[key] = format = "%s %d%s" % (
            baseformat, numremain, lastfield and "s" or "x")
    return struct.unpack(format, theline)
