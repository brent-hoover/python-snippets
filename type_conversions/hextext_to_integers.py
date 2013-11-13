#!/usr/bin/env python
# encoding: utf-8


def hextext_to_integers(htext):
	"""
	htext is a text representation of binary data in hex format
	to make all remaining operations sane, we convert this to a list(array) of ints
	"""
	junk_list_as_ints = list()
	#iterate over htext two characters at a time then convert that 
	#2 character "chunk" to an integer to build a "junk_list" of integers
	#representing the binary data that the clients send
	for (op, code) in zip(htext[0::2], htext[1::2]):
		x = op + code
		y = int(x, 16)
		junk_list_as_ints.append(y)
	return junk_list_as_ints
	
if __name__ == '__main__':
	hextext = "2a"
	x = hextext_to_integers(hextext)
	assert x[0] == 42