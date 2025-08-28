lst = "AabDdegOoPpQqR@"
a = input()
total = 0
for i in range(len(a)):
    if a[i] in lst :
        total += 1
    elif a[i] == "B" :
        total += 2
print(total)