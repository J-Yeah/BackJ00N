import sys
input = sys.stdin.readline

pairs = {')': '(', ']': '['}

while(True):
    sen = input().rstrip()

    stack = list()
    if sen == '.': # . 이 들어오면 종료
        break

    for i in sen:
        if i in '([' :
            stack.append(i)
        elif i in ')]': 
            if not stack or stack[-1] != pairs[i]:
                stack.append(i)
                break
            stack.pop()

    if not stack :
        print('yes')
    else:
        print('no')