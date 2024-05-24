import sys

num = int(sys.stdin.readline())
if num!= 0:
    word = list(sys.stdin.readline())
    for i in range(num-1):
        word1 = sys.stdin.readline()
        for n in range(len(word)):
            if word[n] != word1[n]:
                word[n] = '?'

    for i in range (len(word)) :
        print(word[i], end='')