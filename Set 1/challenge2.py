"""
cryptopals.challenge_one.two
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed XOR.

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179

"""

TEST_STRING_A = "1c0111001f010100061a024b53535009181c"
TEST_STRING_B = "686974207468652062756c6c277320657965"
TARGET_STRING = "746865206b696420646f6e277420706c6179"


def xor_bytes(a: bytes, b: bytes) -> bytes:
	return bytes(a ^ b for a, b in zip(a, b))


if __name__ == "__main__":
	a = bytes.fromhex(TEST_STRING_A)
	b = bytes.fromhex(TEST_STRING_B)
	xor_result = xor_bytes(a, b)

	if xor_result.hex() == TARGET_STRING:
		print("Success!")
	else:
		print("XOR operation failed.")