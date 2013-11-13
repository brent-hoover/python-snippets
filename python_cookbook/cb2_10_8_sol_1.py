def process_mailbox(mailboxname_in, mailboxname_out, filter_function):
    mbin = mailbox.PortableUnixMailbox(file(mailboxname_in,'r'))
    fout = file(mailboxname_out, 'w')
    for msg in mbin:
        if msg is None: break
        document = filter_function(msg, msg.fp.read())
        if document:
            assert document.endswith('\n\n')
            fout.write(msg.unixfrom)
            fout.writelines(msg.headers)
            fout.write('\n')
            fout.write(document)
    fout.close()
