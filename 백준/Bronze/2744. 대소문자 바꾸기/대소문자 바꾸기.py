import sys

word =sys.stdin.readline().rstrip()
word_2 = list()

for i in range(len(word)):
    if word[i].isupper():
        word_2.append(word[i].lower())
    else :
        word_2.append(word[i].upper())

for i in range(len(word)):
    print(word_2[i], end='')