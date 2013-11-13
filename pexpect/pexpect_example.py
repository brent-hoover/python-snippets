import pexpect
password = open("config/qlive.auth", "r").readline().strip()
p = pexpect.spawn("sudo bash install_dynamicctrl.sh")
i = p.expect([".ssword:*", pexpect.EOF])
p.sendline(password)
