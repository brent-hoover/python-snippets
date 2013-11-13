# Ensure the IP address is proper
        try:
            quad = map(int, ip.split('.'))
        except ValueError:
            pass
        else:
            if len(quad)==4 and min(quad)>=0 and max(quad)<=255:
                # Increase by 1 if IP exists; else set hit count = 1
                ipHitListing[ip] = ipHitListing.get(ip, 0) + 1
