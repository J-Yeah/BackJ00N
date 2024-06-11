a = input()
b = int(input())
word = list(a)
word_r = list(reversed(word))

if word == word_r :
    print("YES")
else :
    print("NO")