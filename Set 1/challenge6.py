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
from challenge3 import guess_key


FILE = "6.txt"
TEST_ONE = "this is a test"
TEST_TWO = "wokka wokka!!!"


def hamming(str1: bytes, str2: bytes):
	return sum(bin(a ^ b).count("1") for a, b in zip(str1, str2))



if __name__ == "__main__":
	print(hamming(TEST_ONE.encode(), TEST_TWO.encode()))

	with open(FILE, 'rb') as f:
		edit_distances = []
		contents = f.read()
		for key_size in range(2, 41):

			bytes = int(len(contents) / key_size)

			sum_distance = 0.0
			for i in range(bytes-1):
				edit_distance = hamming(contents[(i*key_size):(i+1)*key_size], contents[(i+1)*key_size:(i+2)*key_size])
				normalized_distance = edit_distance / key_size
				sum_distance += normalized_distance

			avg_distance = sum_distance / bytes
			edit_distances.append((key_size, avg_distance)) 

		min_distances = sorted(edit_distances, key=operator.itemgetter(1))
		print(min_distances)

		candidate_keys = list(key_size for key_size, distance in min_distances[:9])

		for key in candidate_keys:
			print(f"KEY: {key}")
			byte_chunks = [contents[i:i+key] for i in range(0, len(contents), key)]

			transposed_blocks = [b''.join([b[i:i+1] for b in byte_chunks]) for i in range(key)]
			print(f"NUM BLOCKS {len(transposed_blocks)}")
			vigenere_key = ''
			for block in transposed_blocks:
				single_key, decoded, score = guess_key(block)
				vigenere_key += chr(single_key)

			print(vigenere_key)

			# for i in range(key):
			# 	print(b''.join([b[i:i+1] for b in byte_chunks]))






