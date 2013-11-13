m0 = memory()
    ## section of code you're monitoring
    m1 = memory(m0)
    print 'The monitored section consumed', m1, 'bytes of virtual memory'.
