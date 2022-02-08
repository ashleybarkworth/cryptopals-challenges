"""
cryptopals.challenge_one.four
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

import operator
import string
from challenge3 import guess_key

STRINGS_FILE = "strings.txt"

def get_best_fit(lines):
	current_best_fit = None
	current_best_score = -1

	for line in lines:
		key, decoded, score = guess_key(line)

		if current_best_score < 0 or score < current_best_score:
			current_best_fit = (key, decoded, score)
			current_best_score = score

	return current_best_fit


if __name__ == "__main__":
	with open(STRINGS_FILE) as f:
 		lines = [bytes.fromhex(line.strip()) for line in f]
 		key, decoded, score = get_best_fit(lines)


	print(f"KEY: {chr(key)}\nPLAINTEXT: {decoded}\nSCORE: {score}\n")
