from collections import deque
import sys
sys.setrecursionlimit(10000)


t=int(input()) #테스트 케이스


def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상,하,좌,우 확인
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y

        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
            arr[nx][ny]=-1
            dfs(nx,ny)


for i in range(t):
    m, n, k = map(int, input().split())  # 가로 세로 좌표
    arr = [[0]*m for _ in range(n)] # [[0] * m for i in range(n)]
    cnt = 0

    for i in range(k):
        x,y=map(int, input().split())
        arr[y][x]=1

    for q in range(n): #1인 좌표를 bfs탐색
        for w in range(m):
            if arr[q][w] == 1:
                dfs(q, w)
                cnt += 1
    print(cnt)
