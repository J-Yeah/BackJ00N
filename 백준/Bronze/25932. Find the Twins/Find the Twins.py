for _ in range(int(input())):
    a = input()
    b = list(a.split())
    print(a)
    if "18" in a and "17" in a :
        print("both")
    elif "18" in a :
        print("mack")
    elif "17" in a :
        print("zack")
    else :
        print("none")
    print("")