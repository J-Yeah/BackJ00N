n = int(input())
a = list(map(int, input().split()))
su = 0
for i in a :
    if i%2 :
        su += i+1
    else :
        su += i
print(su//2)