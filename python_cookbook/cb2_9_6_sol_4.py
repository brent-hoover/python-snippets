# Tell thread to increment twice
counter.send('increment')
counter.send('increment')
# Request the thread's current value, then print the thread's response
counter.send((cg.self(), 'value'))
print response.receive()
# Tell thread to increment one more time
counter.send('increment')
# Again, request the thread's current value, then print the thread's response
counter.send((cg.self(), 'value'))
print response.receive()
# Tell the thread to stop running
counter.send('stop')
