l,s = map(str, input().split())
if s == 'miss' :
    print(0)
elif s == 'bad' :
    print(200*int(l))
elif s == 'cool' :
    print(400*int(l))
elif s == 'great' :
    print(600*int(l))
elif s == 'perfect' :
    print(1000*int(l))