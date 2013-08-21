from Crypto.Cipher import AES
my_hex = "00"*32
import struct
import string

def main():
	my_binary = ''

	for (op, code) in zip(my_hex[0::2], my_hex[1::2]):
		x = op + code
		y = int(x, 16)
		z = struct.pack('B', y)
		my_binary += z
	print my_binary
	print(len(my_binary))
	aes = AES.new(key=my_binary, mode=AES.MODE_CBC)
	encry = aes.encrypt('deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef')
	print(encry)
	print aes.decrypt(encry)
	happy_hex = ''
	for t in encry:
		h = '%x' % struct.unpack('B', t)
		if len(h) == 1:
			h = '0' + h
		happy_hex += h
	print happy_hex
if __name__ == '__main__':
	main()
    