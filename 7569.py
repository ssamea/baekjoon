from collections import deque
import sys
r = sys.stdin.readline

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        a, b, c = q.popleft()
        visited[c][a][b]=1

        for i in range(6):
            nx=dx[i]+a
            ny=dy[i]+b
            nz=dz[i]+c

            if 0<=nx<n and 0<=ny<m and 0<=nz<h and arr[z][x][y]==0 and visited[z][x][y]==0:
                q.append([nx,ny,nz])
                arr[nz][nx][ny]+=1
                visited[nz][nx][ny]=1

m,n,h = map(int,r().split()) # m=가로 n=세로 h=높이

arr = [[] for _ in range(h)]
visited=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q=deque()
isTrue = False
st = False

for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, r().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append([x,y,z])

bfs()

max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, arr[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num - 1)