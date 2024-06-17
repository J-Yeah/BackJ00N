a = int(input())

for i in range(1, a):
    print(" "*(a-i-1),"*"*(2*i-1))
print("*"*(2*a-1))
