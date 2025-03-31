import sys
input = sys.stdin.readline
from collections import Counter
import math

def ave(lst,n):
    aver = sum(lst)/n
    if aver >= 0:
        return math.floor(aver + 0.5) 
    else: 
        return math.ceil(aver - 0.5)
    
def middle(lst):
    lst.sort()
    return lst[len(lst)//2]

def mode(lst):
    count = Counter(lst)
    max_freq = max(count.values())
    modes = sorted([num for num, freq in count.items() if freq == max_freq])
    if len(modes) > 1 :
        return modes[1]
    else :
        return modes[0]

def ran(lst):
    return max(lst)-min(lst)

a = list()
n = int(input())
for _ in range(n):
    x = int(input())
    a.append(x)

print(ave(a,n))
print(middle(a))
print(mode(a))
print(ran(a))