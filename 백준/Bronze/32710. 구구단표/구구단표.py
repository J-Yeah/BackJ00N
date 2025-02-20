a = int(input())
total = 0
for i in range(1,10):
    if a%i == 0 and a//i <= 9 :
        total = 1
print(total)