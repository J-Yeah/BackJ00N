# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력

a=int(input())

if (a>89):
    print("A")
elif (a>79):
    print("B")
elif (a>69):
    print("C")
elif (a>59):
    print("D")
else:
    print("F")