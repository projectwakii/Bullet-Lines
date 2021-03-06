#!/usr/bin/python3

import pyperclip

# Text must be COPIED into clipboard already. Will be using Keyboard
# Maestro to "Cmd + C" highlighted text at this point in time.

# Get imported text
corpus = pyperclip.paste()

# Manipulate it
# Make corpus into an array
corpusArray = []
for i in range(0, len(corpus)):
    corpusArray.append(corpus[i])

# Add a newline
increment = 0 # see below

for i in range(0, len(corpus)): # indexing starts from 0
    if corpus[i] == "•": #note that every time a bullet point is inserted, the index actually changes +1
    # eg with just this:
    #    the input is a•ab•abc•abcd•abcde
    #    corpusArray.insert(i, "\n")
    # corpusArray becomes this:
    #    ['a', '\n', '•', 'a', '\n', 'b', '•', 'a', '\n', 'b', 'c', '•', ...]
    # so we need to make sure to add an increment, to make sure it's inserted at the right place
        corpusArray.insert((i + increment), "\n")
        increment += 1

# Unarray it, converting it back to a normal string
print(corpusArray)
newCorpus = ''.join(corpusArray)
print("Final result: " + newCorpus)

# Paste it
pyperclip.copy(newCorpus)

# The final step, not in this code, is to physically press "Cmd + V" in order
# to paste it into the document. Again, we'll use Keyboard Maestro.
