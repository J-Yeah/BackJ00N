import string

a = input()
num = 0

for n in range(26) :
    s = list(a)
    for i in range(len(s)):
        s[i]=s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    try :
        s.index('i')
    except :
        num += 1

if num == 0:
    print("impossible")
else :
    print(num)