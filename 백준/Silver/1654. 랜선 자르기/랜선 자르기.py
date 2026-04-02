import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lst = list()
for i in range(k):
  lst.append(int(input()))

start = 1
end = max(lst)

while(start <= end):
  mid = (start + end) // 2
  cnt = 0

  for line in lst:
    cnt += line//mid
    
  if cnt >= n :
    start = mid+1
  else :
    end = mid-1

print(end)