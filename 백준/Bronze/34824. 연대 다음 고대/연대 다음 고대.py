import sys
input = sys.stdin.readline
for i in range(int(input())):
    a = input().strip()
    if a == "yonsei" :
        yon = i
    elif a == "korea" :
        kor = i
if yon > kor :
    print("Yonsei Lost...")
else :
    print("Yonsei Won!")