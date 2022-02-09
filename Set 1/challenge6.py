"""
cryptopals.challenge_one.six
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is officially on, now.

This challenge isn't conceptually hard, but it involves actual error-prone coding. 
The other challenges in this set are there to bring you up to speed. This one is there to qualify you. 
If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

Write a function to compute the edit distance/Hamming distance between two strings. 
The Hamming distance is just the number of differing bits. The distance between:

this is a test

and

wokka wokka!!!

is 37. Make sure your code agrees before you proceed.

For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key. 
You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

Now transpose the blocks: make a block that is the first byte of every block, 
and a block that is the second byte of every block, and so on.

Solve each block as if it was single-character XOR. You already have code to do this.

For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. 
Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. 
Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. 
But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.

"""
import operator
from base64 import b64decode
from challenge3 import guess_key


def hamming_distance(s1: bytes, s2: bytes) -> int:
	"""Compute the Hamming distance between two inputs."""
	assert len(s1) == len(s2)
	return sum(bin(a ^ b).count("1") for a, b in zip(s1, s2))


def split_into_chunks(text, size):
	chunks = [
		text[i:i + size]
		for i in range(0, len(text), size)
		if i < len(text) - size
	]
	return chunks


def guess_keysize(contents):

	distances = []
	for key_size in range(2, 41):
		assert key_size < len(contents) / 2

		# Ciphertext broken up into KEYSIZE chunks
		chunks = split_into_chunks(contents, key_size)

		# First and second blocks of ciphertext
		blocks = [
			contents[0:key_size],
			contents[key_size:key_size * 2]
		]

		hamming_distances = [
	    	[hamming_distance(block, chunk) for chunk in chunks]
			for block
			in blocks
	  	][0]

		avg_distance = sum(hamming_distances) / len(hamming_distances)
		normalized_distance = avg_distance / key_size
		distances.append((key_size, normalized_distance))

	return sorted(distances, key=operator.itemgetter(1))[0]


if __name__ == "__main__":
	assert hamming_distance("this is a test".encode(), "wokka wokka!!!".encode()) == 37

	with open("data/6.txt") as f:
		contents = b64decode(f.read())
		key_size = guess_keysize(contents)[0]
		byte_chunks = split_into_chunks(contents, key_size)

		transposed_blocks = [b''.join([b[i:i+1] for b in byte_chunks]) for i in range(key_size)]
		vigenere_key = ''
		for block in transposed_blocks:
			single_key, decoded, score = guess_key(block)
			vigenere_key += chr(single_key)


		print(f"KEY: {vigenere_key}")





