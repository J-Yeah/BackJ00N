while True :
    try:
        a = input()
        b = ''
        for j in range(len(a)):
            if a[j] == 'i' : b += 'e'
            elif a[j] == 'e' : b += 'i'
            elif a[j] == 'I' : b += 'E'
            elif a[j] == 'E' : b += 'I'
            else : b += a[j]
        print(b)
    except:
        break