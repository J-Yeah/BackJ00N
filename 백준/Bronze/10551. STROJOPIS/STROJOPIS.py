word = ["1QAZ","2WSX","3EDC","4RFV5TGB",
"6YHN7UJM","8IK,","9OL.","0P;/-[\'=]"]
cnt = [0]*8
a = input()
for c in a:
    for i in range(8):
        if c in word[i]:
            cnt[i] += 1
for n in cnt:
    print(n)