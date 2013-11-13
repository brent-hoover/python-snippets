import email.Parser
import os, sys
def main():
    if len(sys.argv) != 2:
        print "Usage: %s filename" % os.path.basename(sys.argv[0])
        sys.exit(1)
    mailFile = open(sys.argv[1], "rb")
    p = email.Parser.Parser()
    msg = p.parse(mailFile)
    mailFile.close()
    partCounter = 1
    for part in msg.walk():
        if part.get_main_type() == "multipart":
            continue
        name = part.get_param("name")
        if name == None:
            name = "part-%i" % partCounter
        partCounter += 1
        # In real life, make sure that name is a reasonable filename 
        # for your OS; otherwise, mangle that name until it is!
        f = open(name, "wb")
        f.write(part.get_payload(decode=1))
        f.close()
        print name
if __name__=="__main__":
    main()
