word = input()

res = [-1] * 26

for i in word:
    a = ord(i) - 97
    res[a] = word.index(i)

for i in res:
    print(i, end = " ")
