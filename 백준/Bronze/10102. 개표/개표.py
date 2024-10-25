n = int(input())
v = input()
if v.count('A')>v.count('B') :
	print('A')
elif v.count('A')<v.count('B') :
	print('B')
else :
	print("Tie")