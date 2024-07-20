num = int(input())
for i in range(num) :
	a = list(map(int, input().split()))
	print(sum(a))