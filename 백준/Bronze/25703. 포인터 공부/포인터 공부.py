n = int(input())
print("int a;")
if n > 0 :
    print("int *ptr = &a;")
if n > 1 :
    print("int **ptr2 = &ptr;")
if n > 2 :
    for i in range(3, n+1):
        print(f"int {'*'*i}ptr{i} = &ptr{i-1};")