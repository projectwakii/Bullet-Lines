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
for i in range(0, len(corpus)): # indexing starts from 0
    if corpus[i] == "•":
        corpusArray.insert(i, "\n")

# Unarray it, converting it back to a normal string
newCorpus = ''.join(corpusArray)
print("Final result: " + newCorpus)

# Paste it
pyperclip.copy(newCorpus)

# The final step, not in this code, is to physically press "Cmd + V" in order
# to paste it into the document. Again, we'll use Keyboard Maestro. 
