"""
cryptopals.challenge_two.one
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"

... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"

"""

def pkcs7_padding(byte_string, block_length):
	bytes_length = len(byte_string)

	if bytes_length < block_length:
		padding_length = block_length - (bytes_length % block_length)
	else:
		padding_length = 0

	padding = bytes([padding_length]) * padding_length
	return b''.join([byte_string, padding])



if __name__ == "__main__":
	padded_string = pkcs7_padding("YELLOW SUBMARINE".encode("utf-8"), 20)

	if padded_string == b'YELLOW SUBMARINE\x04\x04\x04\x04':
		print("Success!")
	else:
		print("Error occurred while padding.")