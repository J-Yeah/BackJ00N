n = input()
s = input()
t = input()
print(sum(ch1 != ch2 for ch1, ch2 in zip(s,t)))