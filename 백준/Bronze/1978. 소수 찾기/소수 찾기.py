import math

num = int(input())
lst = list(map(int, input().split()))
answer = 0

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(num):
    if lst[i] != 0 and lst[i] != 1 :      
        if prime(lst[i]) == True:
            answer += 1
print(answer)