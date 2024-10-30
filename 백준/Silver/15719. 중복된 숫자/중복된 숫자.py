import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline()
s = 0
temp = ""
for num in a:
    if num.isdigit():
        temp += num
    elif num == ' ' :
        s += int(temp)
        temp = ""

s += int(temp)
        
print(s-(n-1)*n//2)