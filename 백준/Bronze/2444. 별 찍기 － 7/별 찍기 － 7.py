num = int(input())

for i in range(1, num):
    print(" "*(num-i-1),"*"*(i*2-1))
print("*"*(num*2-1))
for i in range(num-1, 0, -1):
    print(" "*(num-i-1),"*"*(i*2-1))
