response = cg.Receiver()
response.addHandler((counter, int), lambda msg: msg[1], cg.Message)
