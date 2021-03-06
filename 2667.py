import sys
sys.setrecursionlimit(10000)

def dfs(graph,cnt,x,y):
    graph[x][y]=0 # 왜 0인가? 이미 탐지했으니 0으로 해준거라 생각하면 된다.

    for i in range(4): #왼쪽, 오른쪽, 위쪽, 아래쪽 탐색을 위한 반복문
        nx=x+dx[i] #x값 좌표
        ny=y+dy[i] #y값 좌표

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny]==1:
                cnt=dfs(graph,cnt+1,nx,ny)
    return cnt

n= int(input())
graph=[list(map(int,list(input()))) for _ in range(n)]
# 방문 내역 저장용 ans
ans=[]

# 위 아래 왼 오 방향이동용 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1: #그래프에서 값이 1인 경우에만 dfs 탐색 시작
            ans.append(dfs(graph,1,i,j))
print(len(ans))

for i in sorted(ans):
    print(i)
