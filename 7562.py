import sys
r = sys.stdin.readline
from _collections import deque

n=int(r())

def bfs(x, y, tx, ty):
    q = deque()
    q.append([x, y])
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        a, b = q.popleft()

        if a == tx and b == ty:
            print(arr[tx][ty])
            return

        for i in range(8):
            nx = dx[i]+a
            ny = dy[i]+b

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    arr[nx][ny] = arr[a][b]+1


for _ in range(n):
    l = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())

    arr = [[0]*l for i in range(l)]
    bfs(x, y, tx, ty)





