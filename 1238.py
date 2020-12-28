#파티
#N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티
# 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비, M개의 단방향 도로
#두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다.
import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

def dij(x):
    d = [INF]*n
    heapq.heappush(heap, [0, x])
    d[x] = 0
    while heap:
        w, x = heapq.heappop(heap)
        for nw, nx in a[x]:
            nw += w
            if nw < d[nx]:
                d[nx] = nw
                heapq.heappush(heap, [nw, nx])
    return d

n, m, t = map(int, input().split())
a = [[]*n for _ in range(n)]
heap = []

for i in range(m):
    x, y, w = map(int, input().split())
    a[x-1].append([w, y-1])

ans = [0]*n
for i in range(n):
    d = dij(i)
    ans[i] += d[t-1]
    d = dij(t-1)
    ans[i] += d[i]
print(max(ans))