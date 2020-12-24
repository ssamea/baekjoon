n= int(input())
graph=[list(map(int,list(input()))) for _ in range(n)]
# 방문 내역 저장용 visited
visited = [[0]*n for _ in range(n)]

# 위 아래 왼 오 방향이동용 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(input())

print(graph)