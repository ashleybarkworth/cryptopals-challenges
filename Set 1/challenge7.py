"""
cryptopals.challenge_one.seven
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".

(case-sensitive, without the quotes; exactly 16 characters; 
I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

"""


from base64 import b64decode
from Crypto.Cipher import AES


def aes_ecb_dec(key: bytes, ciphertext: bytes) -> bytes:
	algorithm = AES.new(key, AES.MODE_ECB)
	return algorithm.decrypt(ciphertext)


if __name__ == "__main__":
    with open("data/7.txt") as f:
        contents = f.read()
	
    ciphertext = b64decode(contents)
    plaintext = aes_ecb_dec(b'YELLOW SUBMARINE', ciphertext)

    print(f"{plaintext=}")

