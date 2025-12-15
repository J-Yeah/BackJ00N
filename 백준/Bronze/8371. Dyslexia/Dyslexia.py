n = int(input())
a = input()
b = input()
print(sum(x != y for x, y in zip(a, b)))