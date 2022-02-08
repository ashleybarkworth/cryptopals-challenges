"""
cryptopals.challenge_one.three
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. 
Evaluate each output and choose the one with the best score.
"""

import string
import re
import operator
from collections import Counter
import math

from challenge2 import xor_bytes


TEST_STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

FREQUENCY_TABLE = {
    "a": 0.07743208627550165,
    "b": 0.01402241586697527,
    "c": 0.02665670667329359,
    "d": 0.04920785702311875,
    "e": 0.13464518994079883,
    "f": 0.025036247121552113,
    "g": 0.017007472935972733,
    "h": 0.05719839895067157,
    "i": 0.06294794236928244,
    "j": 0.001267546400727001,
    "k": 0.005084890317533608,
    "l": 0.03706176274237046,
    "m": 0.030277007414117114,
    "n": 0.07125316518982316,
    "o": 0.07380002176297765,
    "p": 0.017513315119093483,
    "q": 0.0009499245648139707,
    "r": 0.06107162078305546,
    "s": 0.061262782073188304,
    "t": 0.08760480785349399,
    "u": 0.030426995503298266,
    "v": 0.01113735085743191,
    "w": 0.02168063124398945,
    "x": 0.0019880774173815607,
    "y": 0.022836421813561863,
    "z": 0.0006293617859758195,
}


def get_chi_squared(input: str) -> float:
	input_len = len(input)
	input_freqs = {chr(b): input.count(chr(b)) / input_len for b in range(256)}

	coefficient = sum(
		abs(expected_frequency - input_freqs[letter])
		for letter, expected_frequency in FREQUENCY_TABLE.items()
	)

	return coefficient;


def guess_key(encoded: bytes) -> tuple:
	scores = []

	for candidate_key in range(256):
		decoded = ''.join(chr(b ^ candidate_key) for b in encoded)
		score = get_chi_squared(decoded)
		scores.append([candidate_key, decoded, score])

	scored = sorted(scores, key=operator.itemgetter(2))
	return scored[0]


if __name__ == "__main__":
	byte_string = bytes.fromhex(TEST_STRING)
	key, decoded, score = guess_key(byte_string)

	print(f"KEY: {chr(key)}\nPLAINTEXT: {decoded}\nSCORE: {score:.2f}\n")

