# 벽 부수고 이동하기
#0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
#bfs로 해보자
# 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
import sys
r = sys.stdin.readline
from _collections import deque

n, m = map(int,r().split())
cnt=0
arr = []

for i in range(n):
    arr.append(list(map(int,input())))


def bfs(x,y):
    q=deque()
    q.append([x,y,1]) # 큐에 삽입, 마지막 1은 벽을 부술 수 있는 기회이다.
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1

    while q:
        a,b,c = q.popleft()

        if a == n - 1 and b == m - 1:
            return visit[a][b][c]

        for i in range(4):
            nx = dx[i]+a
            ny = dy[i]+b

            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny][c] == 0 and arr[nx][ny]==0:
                    arr[nx][ny][c]=arr[a][b][c]+1
                    q.append([nx, ny, c])

                elif arr[nx][ny] == 1 and c == 1:
                    visit[nx][ny][0]= visit[a][b][1]+1

                else:
                    return None
    return arr[nx][ny]

res=bfs(0,0)
if res == None:
    print("-1")

else:
    print(bfs(0,0))