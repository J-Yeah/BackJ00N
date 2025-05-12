a = input()
b = input()
c = input()
try :
    a = int(a)
    n = a+3
except :
    pass
try :
    b = int(b)
    n = b+2
except :
    pass
try :
    c = int(c)
    n = c+1
except :
    pass
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0 :
    print("Buzz")
else :
    print(n)