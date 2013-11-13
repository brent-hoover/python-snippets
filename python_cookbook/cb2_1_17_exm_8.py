msg = string.Template('an $adj $msg')
adj = 'interesting'
print msg.substitute(locals(), msg='message')
# emits an interesting message
