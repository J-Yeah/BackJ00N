import sys
input = sys.stdin.readline
n = int(input())
rec = input().split()
lst = input().split()
for i in lst :
    rec.remove(i)
print(rec[0])