# Your code here
import re

with open("applications/histo/robin.txt") as f:
    words = f.read()
words = re.sub(r'[^A-Za-z0-9\' ]+', ' ', words).lower()
words = words.split(' ')

histogram = {}
longest_word_length = 0
for word in words:
    if word == '':
        continue
    if word in histogram:
        histogram[word][0] += 1
        histogram[word][1] += '#'
    else:
        histogram[word] = [1, '#']
        if len(word) > longest_word_length:
            longest_word_length = len(word)

longest_word_length += 2

print('---------------------------------------  Ordered by Word  ----------------------------------------------')
for key in sorted(histogram):
    print(f'{key:{longest_word_length}}{histogram[key][1]}')

print('-------------------------------------  Ordered by Frequency  -------------------------------------------')

for value in sorted(histogram.items(), key = lambda e: e[1][0], reverse=True):
    print(f'{value[0]:{longest_word_length}}{value[1][1]}')

