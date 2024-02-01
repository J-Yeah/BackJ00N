a = int(input())
num = 1
total = 0

for i in range(a) :
    word = input()
    if word[0] == 'O' :
        total+= 1
    for j in range(1, len(word)) :
        if word[j] == 'O' and word[j-1] == 'O' :
            num += 1
            total += num
        elif word[j] == 'O' :
            total += 1
        else :
            num = 1
    print(total)
    total = 0
    num = 1