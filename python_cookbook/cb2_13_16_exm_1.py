import socket
SERVER = 'irc.freenode.net'
PORT = 6667
NICKNAME = 'logging_bot'
CHANNEL = '#test_py'
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def irc_conn():
    IRC.connect((SERVER, PORT))
def send_data(command):
    IRC.send(command + '\n')
def join(channel):
    send_data("JOIN %s" % channel)
def login(nickname, username='user', password=None,
          realname='Pythonist', hostname='Helena', servername='Server'):
    send_data("USER %s %s %s %s" %
               (username, hostname, servername, realname))
    send_data("NICK %s" % nickname)
irc_conn()
login(NICKNAME)
join(CHANNEL)
filetxt = open('/tmp/msg.txt', 'a+')
try:
    while True:
        buffer = IRC.recv(1024)
        msg = buffer.split()
        if msg[0] == "PING":
            # answer PING with PONG, as RFC 1459 specifies
            send_data("PONG %s" % msg[1])  
        if msg [1] == 'PRIVMSG' and msg[2] == NICKNAME:
            nick_name = msg[0][:msg[0].find("!")]
            message = ' '.join(msg[3:])
            filetxt.write(nick_name.lstrip(':') + ' -> ' +
                          message.lstrip(':') + '\n')
            filetxt.flush()
finally:
    filetxt.close()
