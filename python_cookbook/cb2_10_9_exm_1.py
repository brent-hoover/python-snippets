def main(mailbox_path):
    addresses = set()
    mb = mailbox.PortableUnixMailbox(file(mailbox_path))
    for msg in mb:
        toaddr = msg.getaddr('To')[1]
        addresses.add(toaddr)
    for address in sorted(addresses):
        print address
