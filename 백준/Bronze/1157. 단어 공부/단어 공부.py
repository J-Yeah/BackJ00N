word = input().upper()

sp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num1 = 0

for i in range(len(sp)) :
    num = word.count(sp[i])
    if num>num1 :
        num1 = num
        sp1 = sp[i]
    elif num==num1 :
        sp1 = "?"

print(sp1)