n, m = map(int, input().split())
t, s = map(int, input().split())

if n%8==0 :
    Zip = n + (n//8-1)*s
else:
    Zip = n + n//8*s
    
if m%8==0 :
    Dok = m + t + (m//8-1)*(2*t+s)
else:
    Dok = m + t + m//8*(2*t+s)

if Zip<Dok :
    print("Zip")
    print(Zip)
else :
    print("Dok")
    print(Dok)