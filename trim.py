import re
#Read the wordlist.txt file
words = open('wordlist.txt', 'r')
newWords = open('trimmedWords.txt', 'w')
#Replace all words with an apostrophe, to the same word without an apostrophe
#Write word to new txt file
#Word cannot be more than 9 letters due to countdown rules, so we can
# leave out any longer words which will slow the program
for word in words:
    if len(word) <= 9 and len(word) >= 4:
        newWord = re.sub('[^a-zA-Z0-9\n\.]', '', word)
        newWords.write(newWord.lower())
