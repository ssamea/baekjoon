#N명의 학생들을 키 순서대로 줄을 세우려고 한다.
#M은 키를 비교한 회수
from collections import deque

n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]



for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1


def topology():
    res=[]
    q=deque()

    #진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now=q.popleft()
        res.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in res:
        print(i,end=' ')


topology()