def calculateApacheIpHits(logfile_pathname):
   ''' return a dict mapping IP addresses to hit counts '''
    ipHitListing = {}
    contents = open(logfile_pathname, "r")
    # go through each line of the logfile
    for line in contents:
        # split the string to isolate the IP address
        ip = line.split(" ", 1)[0]
        # Ensure length of the IP address is proper (see discussion)
        if 6 < len(ip) <= 15:
            # Increase by 1 if IP exists; else set hit count = 1
            ipHitListing[ip] = ipHitListing.get(ip, 0) + 1
   return ipHitListing
