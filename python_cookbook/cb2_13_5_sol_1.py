def createhtmlmail(subject, html, text=None):
    " Create a mime-message that will render as HTML or text, as appropriate "
    import MimeWriter, mimetools, cStringIO
    if text is None:
        # Produce an approximate textual rendering of the HTML string,
        # unless you have been given a better version as an argument
        import htmllib, formatter
        textout = cStringIO.StringIO()
        formtext = formatter.AbstractFormatter(formatter.DumbWriter(textout))
        parser = htmllib.HTMLParser(formtext)
        parser.feed(html)
        parser.close()
        text = textout.getvalue()
        del textout, formtext, parser
    out = cStringIO.StringIO()           # output buffer for our message
    htmlin = cStringIO.StringIO(html)    # input buffer for the HTML
    txtin = cStringIO.StringIO(text)     # input buffer for the plain text
    writer = MimeWriter.MimeWriter(out)
    # Set up some basic headers. Place subject here because smtplib.sendmail
    # expects it to be in the message, as relevant RFCs prescribe.
    writer.addheader("Subject", subject)
    writer.addheader("MIME-Version", "1.0")
    # Start the multipart section of the message.  Multipart/alternative seems
    # to work better on some MUAs than multipart/mixed.
    writer.startmultipartbody("alternative")
    writer.flushheaders()
    # the plain-text section: just copied through, assuming iso-8859-1
    subpart = writer.nextpart()
    pout = subpart.startbody("text/plain", [("charset", 'iso-8859-1')])
    pout.write(txtin.read())
    txtin.close()
    # the HTML subpart of the message: quoted-printable, just in case
    subpart = writer.nextpart()
    subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
    pout = subpart.startbody("text/html", [("charset", 'us-ascii')])
    mimetools.encode(htmlin, pout, 'quoted-printable')
    htmlin.close()
    # You're done; close your writer and return the message as a string
    writer.lastpart()
    msg = out.getvalue()
    out.close()
    return msg
