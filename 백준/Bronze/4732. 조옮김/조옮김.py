import sys

mu = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

while True :
    lst = list(sys.stdin.readline().split())
    if lst[0] == '***' :
        break
    else :
        num = int(sys.stdin.readline())
        for i in range(len(lst)) :
            try :
                lst[i].index('b')
                lst[i] = lst[i][0]
                lst[i] = mu[(mu.index(lst[i])-1+num)%len(mu)]
            except :
                try :
                    lst[i] = mu[(mu.index(lst[i])+num)%len(mu)]
                except :
                    lst[i] = lst[i][0]
                    lst[i] = mu[(mu.index(lst[i])+1+num)%len(mu)]

        for j in range(len(lst)) :
            print(lst[j], end=' ')
        print()