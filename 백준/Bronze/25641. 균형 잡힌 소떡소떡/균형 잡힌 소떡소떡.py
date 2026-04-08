import sys
input = sys.stdin.readline

n = int(input())
st = input().rstrip()

for i in range(n):
    if st.count('s')==st.count('t') :
        break
    else :
        st = st[1:]

print(st)