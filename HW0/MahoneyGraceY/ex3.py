import string
import heapq

# Parameters:
#   fname - filename
# Output:
#   wordList - list of words that appear in the text
def file_to_wordlist(fname):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) # replaces punctuation with ' '
    wordlist = []
    with open(fname) as file:
        for line in file:
            cleanLine = line.translate(translator).lower()
            wordlist.extend(cleanLine.split())

    # remove BOM
    wordlist[0] = wordlist[0].lstrip('\ufeff')
    return wordlist

# Parameters:
#   wordlist - list of words in a text
# Output:
#   wordfreq - dictionary of unique words and their frequency
def wordlist_to_wordfreq(wordlist):
    wordfreq = {}
    for w in wordlist:
        if w in wordfreq.keys():
            wordfreq[w] = wordfreq[w] + 1
        else:
            wordfreq[w] = 1
    return wordfreq

# Parameters:
#   wordfreq - dictionary of unique words and their frequency
# Output:
#   wordpriority - sorted word list in increasing order of frequency
def wordfreq_to_wordpriority(wordfreq):
    wordpriority = []
    for word, freq in wordfreq.items():
        heapq.heappush(wordpriority, (freq, word))
    return [heapq.heappop(wordpriority) for i in range(len(wordpriority))]


# ## Test
# # file_to_wordlist 
# words = file_to_wordlist('frankenstein.txt')
# print(words[300:320])

# # wordlist_to_wordfreq
# freq = wordlist_to_wordfreq(words)
# print(list(freq.items())[0:20])

# # wordfreq_to_wordpriority
# priority = wordfreq_to_wordpriority(freq)
# print(priority)