while True: 
    word = input()
    if word=="#" :
        break
    word = word.lower()
    a_list = ['a','e','i','o','u']
    for i in a_list :
        word = word.replace(i,'*')

    print(word.count('*'))
