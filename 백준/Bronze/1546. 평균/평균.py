x = int(input())
num = list(map(int, input().split()))

Max = num[0]

for i in range(1,len(num)):
    if num[i]>Max:
        Max = num[i]
        Max_num = i

for i in range(1, len(num)+1):
    num[i-1] = num[i-1]/Max*100

print(sum(num)/len(num))