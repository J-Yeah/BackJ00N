x = list(input())
try :
    a = x.index('U')
    b = x.index('C', a)
    c = x.index('P', b)
    d = x.index('C', c)
    print("I love UCPC")
except :
    print("I hate UCPC")