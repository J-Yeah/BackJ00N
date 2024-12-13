for _ in range(int(input())):
    value1, value2 = map(float, input().split())
    print(round(abs(value1-value2), 1))