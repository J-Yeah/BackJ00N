s = int(input())

for i in range (s) :
    a,b,c = map(int, input().split())

    num = c//a +1
    num2 = c%a
    if num2 == 0 :
        num2 = a
        num -= 1

    print(num2*100+num)