import re
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open("applications/crack_caesar/ciphertext.txt") as f:
    file_text = f.read()
words = re.sub(r'[^A-Za-z0-9 ]+', ' ', file_text)
letters = [char for char in words]
histogram = {}
for letter in letters:
    if not letter.isalpha():
        continue
    if letter in histogram:
        histogram[letter] += 1
    else:
        histogram[letter] = 1

letters_by_frequency = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z']

decipher_key = {}
i = 0
for letter in sorted(histogram.items(), key = lambda e: e[1], reverse=True):
    decipher_key[letter[0]] = letters_by_frequency[i]
    i += 1

deciphered_string = ''
for char in file_text:
    if not char.isalpha():
        deciphered_string += char
        continue
    deciphered_string += decipher_key[char]

print(deciphered_string)
