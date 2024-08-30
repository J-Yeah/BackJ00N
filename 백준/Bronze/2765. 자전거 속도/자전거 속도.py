i = 0
while True :
    a, b, c = map(float, input().split())
    if b == 0 :
        break
    
    i += 1

    r_mile = (a/12)/5280
    h_time = (c/60)/60
    
    l = 3.1415927*r_mile
    d = b*l
    v = d/h_time
    
    print("Trip #{}: {:.2f} {:.2f}".format(i, round(d, 2), round(v,2)))