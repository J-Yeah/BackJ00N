h1,b1 = map(int, input().split())
h2,b2 = map(int, input().split())
n1 = h1*3 + b1
n2 = h2*3 + b2
n = n1-n2
if n == 0 :
    print("NO SCORE")
elif n >= 0 :
    print("1",n)
elif n <= 0 :
    print("2",abs(n))