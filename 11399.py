#첫째 줄에 사람의 수 N
#각 사람이 돈을 인출하는데 걸리는 시간 t
#출력: 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력

n=int(input())
arr=list(map(int,input().split()))
res=0
wt=0
arr=sorted(arr) #오름차순 정렬

for i in range(len(arr)):
    res+=arr[i]*(n-i)

print(res)
