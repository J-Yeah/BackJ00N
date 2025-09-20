import string

x = input()
for a in string.ascii_uppercase :
    if a not in x :
        print(a)