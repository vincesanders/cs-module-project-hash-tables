import random
import re

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()
words = words.split()

# TODO: analyze which words can follow other words
# Your code here
wordsDict = {}
startWords = []
for i in range(len(words)):
    if i == len(words) - 1:
        break
    if words[i] in wordsDict:
        wordsDict[words[i]].append(words[i + 1])
    else:
        wordsDict[words[i]] = [words[i + 1]]
        if words[i][0] == '"' or words[i][0].isupper():
            startWords.append(words[i])

# TODO: construct 5 random sentences
# Your code here
for _ in range(5):
    current = random.choice(startWords)
    found_end = False
    sentence = ''
    while not found_end:
        sentence += current + ' '
        current = random.choice(wordsDict[current])
        last = current[len(current) - 1]
        if last == '.' or last == '?' or last == '!' or last == '"':
            pen_ult = current[len(current) - 2]
            if last == '"' and not (pen_ult == '.' or pen_ult == '?' or pen_ult == '!' or pen_ult == '"'):
                continue
            # stop work
            sentence += current
            print(sentence)
            found_end = True