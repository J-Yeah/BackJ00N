for i in range(1, int(input())+1):
    a = int(input())
    if a <= 25:
        print(f"Case #{i}: World Finals")
    elif a <= 1000 :
        print(f"Case #{i}: Round 3")
    elif a <= 4500 :
        print(f"Case #{i}: Round 2")
    else :
        print(f"Case #{i}: Round 1")