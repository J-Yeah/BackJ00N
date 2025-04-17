a = list()
for _ in range(9):
    s = input()
    a.append(s)
if a.count("Tiger")>a.count("Lion"):
    print("Tiger")
elif a.count("Tiger")<a.count("Lion"):
    print("Lion")