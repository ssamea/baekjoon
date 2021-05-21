#부모찾기
#dfs
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(tree,root,parents):
    for i in tree[root]:
        if parents[i]==0:
            parents[i]=root
            dfs(tree,i,parents)

n=int(input())
tree=[[] for _ in range(n+1)]

#부모저장
parents=[0 for _ in range(n+1)]

#트리 정보 입력 ex) tree=[[],[6,4].[4]..] 이런식으로 각 노드에 연결된 노드들을 넣음
for _ in range(n-1):
    u,w=map(int,input().split())
    tree[u].append(w)
    tree[w].append(u)

dfs(tree,1,parents) #노드1은 시작 노드

for i in range(2,n+1): #2번노드부터 부모노드 출력
    print(parents[i])