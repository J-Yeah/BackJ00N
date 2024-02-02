while True :
    a = input()
    total = 0
    
    if a[0] == '0' :
        break

    for i in range(len(a)):
        if a[i] == a[len(a)-i-1] :
            total += 1

    if total == len(a) :
        print("yes")
    else :
        print("no")