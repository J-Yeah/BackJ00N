a = int(input())
s=0

for i in range(a):
    b = input()
    if b == "Never gonna give you up" or b=="Never gonna let you down" or b=="Never gonna run around and desert you" or b=="Never gonna make you cry" or b=="Never gonna say goodbye" or b=="Never gonna tell a lie and hurt you" or b=="Never gonna stop" :
        s += 1
if a==s :
    print("No")
else :
    print("Yes")