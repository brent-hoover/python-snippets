#!/usr/bin/env python
import base64, quopri
import mimetypes, email.Generator, email.Message
import cStringIO, os
# sample addresses
toAddr = "example@example.com"
fromAddr = "example@example.com"
outputFile = "dirContentsMail"
def main():
    mainMsg = email.Message.Message()
    mainMsg["To"] = toAddr
    mainMsg["From"] = fromAddr
    mainMsg["Subject"] = "Directory contents"
    mainMsg["Mime-version"] = "1.0"
    mainMsg["Content-type"] = "Multipart/mixed"
    mainMsg.preamble = "Mime message\n"
    mainMsg.epilogue = "" # to ensure that message ends with newline
    # Get names of plain files (not subdirectories or special files)
    fileNames = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    for fileName in fileNames:
        contentType, ignored = mimetypes.guess_type(fileName)
        if contentType is None:     # If no guess, use generic opaque type
            contentType = "application/octet-stream"
        contentsEncoded = cStringIO.StringIO()
        f = open(fileName, "rb")
        mainType = contentType[:contentType.find("/")]
        if mainType=="text":
            cte = "quoted-printable"
            quopri.encode(f, contentsEncoded, 1)   # 1 to also encode tabs
        else:
            cte = "base64"
            base64.encode(f, contentsEncoded)
        f.close()
        subMsg = email.Message.Message()
        subMsg.add_header("Content-type", contentType, name=fileName)
        subMsg.add_header("Content-transfer-encoding", cte)
        subMsg.set_payload(contentsEncoded.getvalue())
        contentsEncoded.close()
        mainMsg.attach(subMsg)
    f = open(outputFile, "wb")
    g = email.Generator.Generator(f)
    g.flatten(mainMsg)
    f.close()
    return None
if __name__=="__main__":
    main()
