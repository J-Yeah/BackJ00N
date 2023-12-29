num = int(input())
a = [0,1,2,3,4,5,6,7,8]
a[0] = num
Max = a[0]
b = 1

for i in range (1,9):
    num = int(input())
    a[i] = num
    for j in range(1, i+2):
        if a[j-1]> Max :
            Max = a[j-1]
            b = j
        else:
            pass

print(Max)
print(b)