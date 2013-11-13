if __name__=="__main__":
    import smtplib
    f = open("newsletter.html", 'r')
    html = f.read()
    f.close()
    try:
        f = open("newsletter.txt", 'r')
        text = f.read()
    except IOError:
        text = None
    subject = "Today's Newsletter!"
    message = createhtmlmail(subject, html, text)
    server = smtplib.SMTP("localhost")
    server.sendmail('agillesp@i-noSPAMSUCKS.com',
        'agillesp@i-noSPAMSUCKS.com', message)
    server.quit()
