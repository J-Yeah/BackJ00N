a = int(input())
num = list(map(int, input().split()))
b = 0

for i in range(a) :
    b += num[i]

print((b+(a-1)*8)//24, (b+(a-1)*8)%24)