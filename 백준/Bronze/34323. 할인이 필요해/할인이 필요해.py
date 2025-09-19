n, m, s = map(int, input().split())
c1 = s * (m + 1) * (100 - n) // 100
c2 = m * s
print(min(c1,c2))