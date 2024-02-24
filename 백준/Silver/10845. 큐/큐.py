import sys

n=int(sys.stdin.readline())
num=list()
a=list()

for i in range(n):
    a=sys.stdin.readline().split()
    
    if a[0]=='push':
        num.append(int(a[1]))
        
    elif a[0]=='pop':
        if len(num)<=0:
            print('-1')
        else:
            print(num.pop(0))
            
    elif a[0]=='size':
        print(len(num))
        
    elif a[0]=='empty':
        if len(num)<=0:
            print('1')
        else:
            print('0')
            
    elif a[0]=='front':
        if len(num)!=0:
            print(num[0])
        else:
            print('-1')

    elif a[0]=='back':
        if len(num)<=0:
            print('-1')
        else:
            print(num[-1])