from Crypto.Cipher import AES
from Crypto import Random
import sys
from struct import pack, pack_into
from ctypes import create_string_buffer

test = "SixTeen Byte Dat"
key = b'SixTeen Byte Key' 


def pad_data(unpadded_data):
	x = len(unpadded_data)
	closest_multiple = ((x / 16) + 1) * 16
	length_of_pad = closest_multiple - x
	pad = ' ' * length_of_pad
	padded_data = unpadded_data + pad
	return padded_data

def ascii_to_bin(text):
	int_list = list()
	bin_list = list()
	buff = create_string_buffer(len(text))
	for x in text:
		int_val = ord(x)
		bin_val = bin(int_val)
		bin_list.append(bin_val)
	return bin_list


def main(text_to_crypt):
	assert(sys.byteorder == 'little')
	iv = Random.new().read(AES.block_size)
	#cipher = AES.new(buff, AES.MODE_CBC, iv)
	cipher = AES.new(key, AES.MODE_CFB, iv)

	msg = iv + cipher.encrypt(text_to_crypt)
	print(msg)

	denc = cipher.decrypt(msg)
	print(denc[16:])

if __name__ == '__main__':
	d = pad_data('I have a bunch of hair and its mostly brown')
	main(d)