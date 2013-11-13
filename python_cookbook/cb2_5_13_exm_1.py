def finditer(text, pattern):
    pos = -1
    while True:
        pos = text.find(pattern, pos+1)
	if pos < 0: break
	yield pos
