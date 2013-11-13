import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = 'brent@autoshepherd.com'
toaddrs  = 'brent@autoshepherd.com'


# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
line = 'Test Message'
msg = msg + line

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
