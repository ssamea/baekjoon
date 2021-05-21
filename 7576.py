import sys
from collections import deque
r = sys.stdin.readline

m,n = map(int,r().split()) # m=가로 n=세로

arr = [list(map(int, r().split())) for _ in range(n)]
res = 0
def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    temp = -1
    q = deque()
    q.append([x, y])

    while q:
        temp += 1
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4): # 방향탐색
             nx = dx[i]+a
             ny = dy[i]+b

             if n > nx >= 0 and m > ny >= 0:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[nx][ny]+1
                    q.append([nx, ny])

    for b in arr:
        if 0 in b:
            return -1
    return temp

# 리스트에서 값이 1인 지점을 탐색하여 그 기준으로 bfs
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res = bfs(i,j)

print(res)