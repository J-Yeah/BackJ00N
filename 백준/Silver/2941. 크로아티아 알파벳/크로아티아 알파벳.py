word = input()
a_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in a_list :
    word = word.replace(i,'*')

print(len(word))