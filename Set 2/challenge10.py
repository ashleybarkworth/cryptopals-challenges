"""
cryptopals.challenge_two.two
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

"""

from base64 import b64decode
from Crypto.Cipher import AES
from challenge9 import pkcs7_padding


def xor_bytes(a: bytes, b: bytes) -> bytes:
	return bytes(a ^ b for a, b in zip(a, b))

def ecb_mode(key: bytes, text: bytes, encrypt: bool = False) -> bytes:
	algorithm = AES.new(key, AES.MODE_ECB)
	if encrypt:
		return algorithm.encrypt(text)
	else:
		return algorithm.decrypt(text)

def cbc_mode(iv: bytes, text: bytes, key: bytes, encrypt: bool = False) -> bytes:
	if encrypt:
		ciphertext = b''
		previous_cipher_block = iv

		padded = pkcs7_padding(text, AES.block_size)

		for i in range(0, len(text), len(key)):
			block = pkcs7_padding(text[i:i+len(key)], len(key))
			xored_block = xor_bytes(previous_cipher_block, block)
			cipher_block = ecb_mode(key, xored_block, True)
			ciphertext += cipher_block
			previous_cipher_block = cipher_block

		return ciphertext
	else:
		plaintext = b''
		previous_cipher_block = iv

		for i in range(0, len(text), len(key)):
			block = pkcs7_padding(text[i:i+len(key)], len(key))
			decrypted_block = ecb_mode(key, bytes(block), False)
			plaintext_block = xor_bytes(previous_cipher_block, decrypted_block)
			plaintext += plaintext_block
			previous_cipher_block = block

		return plaintext

if __name__ == "__main__":
	iv = b'\x00' * AES.block_size
	key = b'YELLOW SUBMARINE'
	with open("data/10.txt") as f:
 		text = b64decode(f.read())
 		ciphertext = cbc_mode(iv, text, key, True)
 		plaintext = cbc_mode(iv, ciphertext, key, False)
 		if text == plaintext:
 			print("Success!")
 		else:
 			print("Error occurred during conversions.")
