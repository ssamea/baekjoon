n=int(input())
list=list(map(int,input().split()))
row=[0]*n

for i in range(1,n+1):
    cnt=0
    t=list[i-1]
    for j in range(n):
        if cnt==t and row[j]==0:
            row[j]=i
            break
        elif row[j]==0:
            cnt+=1
print(row)
