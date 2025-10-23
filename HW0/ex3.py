import string
# Parameters:
#   fname - filename
# Output:
#   wordList - list of words that appear in the text
def file_to_wordlist(fname):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) # replaces punctuation with ' '
    wordlist = []
    with open(fname, encoding='utf-8', errors='ignore') as file: # ignores bad chars
        for line in file:
            cleanLine = line.translate(translator).lower()
            wordlist.extend(cleanLine.split())

    # remove BOM
    wordlist[0] = wordlist[0].lstrip('\ufeff')
    return wordlist

def wordlist_to_wordfreq(wordlist):
    wordfreq = {}

    return wordfreq

## Test
# file_to_wordlist 
words = file_to_wordlist('frank.txt')
print(words[200:230])

# wordlist_to_wordfreq
