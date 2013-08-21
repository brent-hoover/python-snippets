from Crypto.Cipher import AES
import hashlist
import struct
import string
import zlib

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

def find_key(junk, device_id):
    """Find the key in junk using CRC

    Args:
        junk: a list of junk in as integers, must be at least 512
        and be treated as a list, not a string
        device_id: the device_id of the client

    :returns: a list of integers that represents the key
    """
    key_list = list()
    # Get an MD5 hex digest of the device_id 
    device_hash = hashlib.md5(device_id).hexdigest() 

    # magick line returns a number < len(junk)
    offset = (zlib.crc32(device_hash)& 0xffffffff) % len(junk)

    # lazy man fix for overflow possibility. theres probably a more robust
    #  way of doing this.
    if offset >= (len(junk)-32):
        offset = (len(junk)-33)

    #Cannot use this, we need to operate on an array, not a string
    return r''.join(junk[offset:offset+32])

def intlist_to_binary(key_list):
	"""
	Convert an extracted list of integers to binary for submission to cryptography library
	so that it matches what the clients intended to send us
	:key_list: an array/list of integers, each representing a "byte" of data
	"""
	bin_chunk = ''
	for x in key_list:
		bin_chunk += struct.pack('B', x)
	return bin_chunk

def intlist_to_hex(int_list):
	"""
	We need to take the list of integers that represents our key as binary
	and convert it to hex (now that we have extracted it from "junk")
	so that it is in a form that can be stored in the database
	(ints create ambiguity, and we can't store binary data natively (check that, if we can: skip))
	"""
	key_ashex = list()
	for x in int_list:
		#convert to hex
		h = '%x' % x
		key_ashex.append(h)  #appending to list avoids problems with string concatenation
	

def init_encryption(hex_string, device_id):
	int_list = hextext_to_integers()
	key_ints = find_key(int_list)
	key_hex = intlist_to_hex(key_insts)
	mid = hashlib.md5(device_id).hexdigest()  #the key of our key value pair to store
	profile_scode = ProfileScode(mid=mid, scode=key_hex)
	crypt_key = keylist_to_binary(key_inst)
	aes = AES.new(key=crypt_key, mode=AES.MODE_CBC)
	return aes

class Grypto(object):

	def __init__(self, hex_text, device_id):
		self.crypto_object = init_encryption(hex_text, device_id)

	def encrypt(data):
		"""
		Return encrypted data to pass back to client
		"""
		return self.crypto_object.encrypt(data)

	def decrypt(data):
		"""
		Decrypt data to send to existing endpoints
		"""
		return self.crypto_object.decrypt(data)

if __name__ == '__main__':
    
    grypto = Grypto(hex_text, device_id)


    