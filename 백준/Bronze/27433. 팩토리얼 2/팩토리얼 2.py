a = int(input())


if a == 0 :
    print(1)
else:
    for i in range(1,a):
        a *= i

    print(a)
