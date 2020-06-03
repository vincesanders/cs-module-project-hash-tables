import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

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
        if words[i][0] == '"' or words[i[0]].isupper():
            startWords.append(words[i])


# TODO: construct 5 random sentences
# Your code here
current = random.choice(startWords)
found_end = false
sentence = ''
while not found_end:
