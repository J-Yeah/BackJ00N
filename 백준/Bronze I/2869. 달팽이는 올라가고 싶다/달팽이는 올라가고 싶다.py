a, b, c = map(int, input().split())

leng = (c-b)//(a-b)

if (c-b)%(a-b) != 0 :
    leng += 1


print(leng)