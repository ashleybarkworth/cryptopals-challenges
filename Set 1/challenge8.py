"""
cryptopals.challenge_one.eight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

"""


def detect_ecb(ciphertext: bytes) -> bool:
	block_size = 16
	blocks = [
		ciphertext[i:i+block_size]
		for i in range(0, len(ciphertext), block_size)
		if i < len(ciphertext) - block_size
	]

	# If there are duplicate blocks, then ECB detection likely
	duplicate_blocks = len(blocks) - len(set(blocks))
	ecb_detected = duplicate_blocks > 0
	return duplicate_blocks, ecb_detected


if __name__ == "__main__":
	with open("data/8.txt") as f:
		lines = [line for line in f]

	for i, line in enumerate(lines):
		ciphertext = bytes.fromhex(line)
		duplicate_blocks, ecb_detected = detect_ecb(ciphertext)
		if ecb_detected:
			print(f"Detected {duplicate_blocks} duplicate blocks on line {i}. ECB encryption likely.")



