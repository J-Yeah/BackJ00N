import sys
while True :
    a = sys.stdin.readline().rstrip()
    num = 0
    if a=='#' :
        break
    for i in range(1, len(a)+1) :
        if a[-i] == '-':
            s = 0
        elif a[-i] == '\\':
            s = 1
        elif a[-i] == '(' :
            s = 2
        elif a[-i] == '@' :
            s = 3
        elif a[-i] == '?' :
            s = 4
        elif a[-i] == '>' :
            s = 5
        elif a[-i] == '&' :
            s = 6
        elif a[-i] == '%' :
            s = 7
        elif a[-i] == '/' :
            s = -1
        num += s*(8**(i-1))
    print(num)