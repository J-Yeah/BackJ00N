word = input()

word_r = list()

for i in range(len(word),0,-1) :
    word_r.append(word[i-1])


total = 0

for i in range(len(word)):
    if word[i]==word_r[i] :
        total += 1
    else :
        break

if total==len(word) :
    print(1)
else:
    print(0)
