N = int(input())
a = [0,1]
for i in range(N-1) :
    a.append(a[i]+a[i+1])
print(a[-1])