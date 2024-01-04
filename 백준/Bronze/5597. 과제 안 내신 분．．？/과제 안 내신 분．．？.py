a = list()
for i in range(1, 31):
    a.append(0)

for i in range(1,29):
    num = int(input())
    a[num-1] = num

for i in range(1, 31):
    if a[i-1]==0:
        print(i)