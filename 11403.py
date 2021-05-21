#경로 찾기
#첫째 줄에 정점의 개수 N
#둘째 줄부터 N개 줄에는 그래프의 인접 행렬
INF=int(1e9)
n=int(input())
#graph=[[INF]*(n) for _ in range(n)]
#graph=[list(map(int,input().split())) for i in range(n)]
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))



for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for i in graph:
    for j in i:
        print(j, end=" ")
    print()