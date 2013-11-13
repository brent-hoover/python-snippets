if __name__ == '__main__':
    print 'Starting Pinhole port forwarder/redirector'
    import sys
    # get the arguments, give help in case of errors
    try:
        port = int(sys.argv[1])
        newhost = sys.argv[2]
        try: newport = int(sys.argv[3])
        except IndexError: newport = port
    except (ValueError, IndexError):
        print 'Usage: %s port newhost [newport]' % sys.argv[0]
        sys.exit(1)
    # start operations
    sys.stdout = open('pinhole.log', 'w')
    Pinhole(port, newhost, newport).start()
