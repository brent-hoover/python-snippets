# Interactive script to clean POP3 mailboxes from malformed or too-large mails
#
# Iterates over nonretrieved mails, prints selected elements from the headers,
# prompts interactively about whether each message should be deleted
import sys, getpass, poplib, re
# Change according to your needs: POP host, userid, and password
POPHOST = "pop.domain.com"
POPUSER = "jdoe"
POPPASS = ""
# How many lines to retrieve from body, and which headers to retrieve
MAXLINES = 10
HEADERS = "From To Subject".split()
args = len(sys.argv)
if args>1: POPHOST = sys.argv[1]
if args>2: POPUSER = sys.argv[2]
if args>3: POPPASS = sys.argv[3]
if args>4: MAXLINES= int(sys.argv[4])
if args>5: HEADERS = sys.argv[5:]
# An RE to identify the headers you're actually interested in
rx_headers  = re.compile('|'.join(headers), re.IGNORECASE)
try:
    # Connect to the POP server and identify the user
    pop = poplib.POP3(POPHOST)
    pop.user(POPUSER)
    # Authenticate user
    if not POPPASS or POPPASS=='=':
        # If no password was supplied, ask for the password
        POPPASS = getpass.getpass("Password for %s@%s:" % (POPUSER, POPHOST))
    pop.pass_(POPPASS)
    # Get and print some general information (msg_count, box_size)
    stat = pop.stat()
    print "Logged in as %s@%s" % (POPUSER, POPHOST)
    print "Status: %d message(s), %d bytes" % stat
    bye = False
    count_del = 0
    for msgnum in range(1, 1+stat[0]):
        # Retrieve headers
        response, lines, bytes = pop.top(msgnum, MAXLINES)
        # Print message info and headers you're interested in
        print "Message %d (%d bytes)" % (msgnum, bytes)
        print "-" * 30
        print "\n".join(filter(rx_headers.match, lines))
        print "-" * 30
        # Input loop
        while True:
            k = raw_input("(d=delete, s=skip, v=view, q=quit) What? ")
            k = k[:1].lower()
            if k == 'd':
                # Mark message for deletion
                k = raw_input("Delete message %d? (y/n) " % msgnum)
                if k in "yY":
                    pop.dele(msgnum)
                    print "Message %d marked for deletion" % msgnum
                    count_del += 1
                    break
            elif k == 's':
                print "Message %d left on server" % msgnum
                break
            elif k == 'v':
                print "-" * 30
                print "\n".join(lines)
                print "-" * 30
            elif k == 'q':
                bye = True
                break
        # Time to say goodbye?
        if bye:
            print "Bye"
            break
    # Summary
    print "Deleting %d message(s) in mailbox %s@%s" % (
        count_del, POPUSER, POPHOST)
    # Commit operations and disconnect from server
    print "Closing POP3 session"
    pop.quit()
except poplib.error_proto, detail:
    # Fancy error handling
    print "POP3 Protocol Error:", detail
