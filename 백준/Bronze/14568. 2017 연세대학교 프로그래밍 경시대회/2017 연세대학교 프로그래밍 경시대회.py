n = int(input())
way = 0
for tack in range(1, n-1) :
    for young in range(1, n-1):
        for nam in range(1, n-1):
            if nam+young+tack == n and nam>=young+2 and tack%2==0 :
                way += 1
print(way)