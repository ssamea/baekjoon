#최소비용 구하기(다읷ㅌ라)
import sys
import heapq

INF = 1e9


def dijkstra(n, s, e, edg):
    q = []
    dist = [INF] * n
    dist[s-1] = 0
    heapq.heappush(q, [s-1, 0])

    while q:
        pos, cost = heapq.heappop(q)

        for p, c in edg[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [p, c])
    return dist[e-1]


N = int(input())
M = int(input())
edges = [[] for _ in range(N)]
for i in range(M):
    u, v, w = list(map(int, input().split()))
    edges[u-1].append([v-1, w])

st, end = map(int, input().split())

print(dijkstra(N, st, end, edges))
