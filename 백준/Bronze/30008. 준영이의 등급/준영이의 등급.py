N, K = map(int, input().split())
G = list(map(int, input().split()))
result = []
 
for i in G:
    P = (i * 100) // N
    if 0 <= P <= 4:
        print(1, end=' ')
    elif 4 < P <= 11:
        print(2, end=' ')
    elif 11 < P <= 23:
        print(3, end=' ')
    elif 23 < P <= 40:
        print(4, end=' ')
    elif 40 < P <= 60:
        print(5, end=' ')
    elif 60 < P <= 77:
        print(6, end=' ')
    elif 77 < P <= 89:
        print(7, end=' ')
    elif 89 < P <= 96:
        print(8, end=' ')
    elif 96 < P <= 100:
        print(9, end=' ')