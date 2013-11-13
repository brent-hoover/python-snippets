import re
    # an IP is: 4 strings, each of 1-3 digits, joined by periods
    ip_specs = r'\.'.join([r'\d{1,3}']*4)
    re_ip = re.compile(ip_specs)
    for line in contents:
        match = re_ip.match(line)
        if match:
            # Increase by 1 if IP exists; else set hit count = 1
            ip = match.group()
            ipHitListing[ip] = ipHitListing.get(ip, 0) + 1
