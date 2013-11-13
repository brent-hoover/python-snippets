#!/usr/bin/env python
""" Extract and print all 'To:' addresses from a mailbox """
import mailbox
def main(mailbox_path):
    addresses = {}
    mb = mailbox.PortableUnixMailbox(file(mailbox_path))
    for msg in mb:
        toaddr = msg.getaddr('To')[1]
        addresses[toaddr] = 1
    addresses = addresses.keys()
    addresses.sort()
    for address in addresses:
        print address
if __name__ == '__main__':
    import sys
    main(sys.argv[1])
