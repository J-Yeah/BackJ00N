while True :
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0 :
        break
    a = a*a
    b = b*b
    c = c*c
    if a == b+c or b == a+c or c == a+b :
        print("right")
    else :
        print("wrong")