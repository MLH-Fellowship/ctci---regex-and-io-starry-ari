# Write the solution for "Longest Word".

import re
with open("../inputs/longest.txt", 'r') as f:
    words = f.read().split()
    longestWord = len(max(words, key=len))
    word = [textword for textword in words if len(textword) == longestWord]
    print('\033[1m' + word[0])
    word = word[0]
    with open("../inputs/longest.txt", 'w') as o:
        o.write(re.sub(word, '\033[1m' + word))




