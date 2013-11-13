def scanner(fileobject, linehandler):
    for line in fileobject:
        linehandler(line)
