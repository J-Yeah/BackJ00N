t1 = list(map(int,input().split()))
t2 = list(map(int,input().split()))
s1 = t1[0]+t1[1]*2+t1[2]*3
s2 = t2[0]+t2[1]*2+t2[2]*3

if s1>s2:
    print(1)
elif s1<s2:
    print(2)
else :
    print(0)