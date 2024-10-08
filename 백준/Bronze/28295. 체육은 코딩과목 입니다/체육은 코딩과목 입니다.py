a = 0
for i in range(10):
    a += int(input())
if a%4 == 0 :
    print("N")
elif a%4 == 1:
    print("E")
elif a%4 == 2:
    print("S")
elif a%4 == 3:
    print("W")