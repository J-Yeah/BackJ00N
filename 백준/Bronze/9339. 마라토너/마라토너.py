import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    stu = list(map(int, input().split()))
    con = list()
    for i in range(int(input())):
        a,b,c = map(int, input().split())
        d = b*60 + c
        if d >= 0 and d <= 360 :
            con.append([a,d])
    con.sort(key = lambda x:x[1])
    cnt = 0
    best = 0
    for y in range(len(con)):
        for x in stu :
            if x == con[y][0] :
                cnt += 1
                if not best :
                    best = x
    print(best, cnt)