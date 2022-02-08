"""
cryptopals.challenge_one.one
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert hex to base 64.

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

"""

from base64 import b64encode


TEST_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
TARGET_STRING = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex2base64(hex: str) -> bytes:
	return b64encode(bytes.fromhex(hex)).decode()


if __name__ == "__main__":
	string_b64 = hex2base64(TEST_STRING)

	if string_b64 == TARGET_STRING:
		print("Success!")
	else:
		print("Conversion failed")
