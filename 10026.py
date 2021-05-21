#적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다
#크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림
#적록색약=r과 g는 같음

import sys
sys.setrecursionlimit(10000)

def dfs(x,y,type):
    visited.append((x,y))
    # 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and ((nx, ny) not in visited):
            # 정상인
            if type == 0 and painting[nx][ny] == painting[x][y]:
                dfs(nx, ny, 0)
            # 적록색맹
            elif type == 1 and painting[nx][ny] == painting[x][y]:
                dfs(nx, ny, 1)



n= int(input())
painting=[list(input()) for _ in range(n)]
cnt1,cnt2=0,0 # cnt1= normal people , cnt2= 적록색약 사람
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


#정상인
visited=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in visited:
            dfs(i,j,0)
            cnt1+=1

#적맹
for i in range(n):
    for j in range(n):
        if painting[i][j]=='G':
            painting[i][j]='R'
visited=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in visited:
            dfs(i,j,1)
            cnt2+=1

print(cnt1,cnt2)