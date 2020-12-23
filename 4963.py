#섬의 갯수
#정사각형으로 이루어져 있는 섬과 바다 지도 => 인접행렬 섬의 개수를 세는 프로그램을 작성하시오.
#너비 w와 높이 h
#왼쪽 체크 시 = 현재 X - 1, 현재 Y + 0
#오른쪽 체크 시 = 현재 X + 1, 현재 Y + 0
#위쪽 체크 시 = 현재 X + 0, 현재 Y - 1
#아랫쪽 체크 시 = 현재 X + 0, 현재 Y + 1
# dx, dy에 상하좌우 + 대각선을 추가하여 자신 기준으로 총 8번을 탐색

import sys
from collections import deque
sys.setrecursionlimit(10000)


dx = [-1, 1, 0, 0, -1, 1, -1, 1] #왼쪽은 -1 오른쪽은 +1 위,아래는 0, 각 대각선 -1,1
dy = [0, 0, -1, 1, -1, 1, 1, -1]
def bfs(x, y):
    queue=deque()#탐색하려는 좌표를 담기
    queue.append((x,y))
    graph[x][y]=0

    while queue:
        now=queue.popleft()
        for i in range(8):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while(True):
    w,h= map(int,input().split())
    if w==0 and h==0:
        break
    graph = []
    cnt=0

    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h): #인접행렬 그래프의 인덱스만큼
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)