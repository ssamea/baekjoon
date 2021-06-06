# 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다
# x > p 그리고 y > q 이어야 더 큰 거임

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
grade=[]
#cnt=1

# 첫번째 인덱스부터 계속 탐색을 시작해보자
for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    grade.append(cnt)


for i in grade:
    print(i, end=' ')

