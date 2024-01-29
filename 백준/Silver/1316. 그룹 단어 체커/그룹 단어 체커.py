num = int(input())
total = 0

for i in range(num) :
    word = input()
    j = 0
    while j<len(word):
        if word.count('*', j,len(word))>0 :
            break
        a = word.count(word[j])
        word = word.replace(word[j],'*')
        if a>1 :
            j += a-1
        if j==len(word)-1 :
            total+=1
        j+= 1

print(total)