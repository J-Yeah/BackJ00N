num = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(num) :
	if a[i]%2==0 :
		total += 1
if total>num//2 :
    print("Happy")
else :
    print("Sad")