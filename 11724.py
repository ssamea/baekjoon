import sys
sys.setrecursionlimit(10000)


node,edge = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]
visited = [False]*(node+1)
cnt = 0

for _ in range(edge):
    u, v =map(int, sys.stdin.readline() .split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(node):
    visited[node]=True #방문처리
    for e in graph[node]:
        if not visited[node]:
            DFS(e)

for j in range(1,node+1):
    if not visited[j]:
        DFS(j)
        cnt += 1

print(cnt)

