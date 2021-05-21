n=int(input())
arr=list(map(int,str(n)))
arr.sort(reverse=True)

for i in arr:
    print(i, end='')