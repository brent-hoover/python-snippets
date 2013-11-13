def fields(baseformat, theline, lastfield=False):
    # by how many bytes does theline exceed the length implied by
    # base-format (struct.calcsize computes exactly that length)
    numremain = len(theline)-struct.calcsize(baseformat)
    # complete the format with the appropriate 's' or 'x' field, then unpack
    format = "%s %d%s" % (baseformat, numremain, lastfield and "s" or "x")
    return struct.unpack(format, theline)
