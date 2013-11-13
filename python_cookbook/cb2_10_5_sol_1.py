def clientCachePercentage(logfile_pathname):
    contents = open(logfile_pathname, "r")
    totalRequests = 0
    cachedRequests = 0
    for line in contents:
        totalRequests += 1
        if line.split(" ")[8] == "304":
            # if server returned "not modified"
            cachedRequests += 1
    return int(0.5+float(100*cachedRequests)/totalRequests)
