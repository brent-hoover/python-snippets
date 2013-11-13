import socket, ftplib
def isFTPSiteUp(site):
    try:
        ftplib.FTP(site).quit()
    except socket.error:
        return False
    else:
        return True
