import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
precede = [0 for _ in range(n + 1)]

heap, result = [], []

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)  # 연결된 간선. x번 문제는 y번보다 먼저 풀어야 한다.
    precede[y] += 1  # 이어진 노드의 진입차수.
    # (y번 문제는 몇 개의 선행문제와 연결되어 있는지. 진입차수라 보면 된다)

for i in range(1, n + 1):
    if precede[i] == 0:
        # 진입차수가 0인, 즉 선행문제 없이 풀어도 되는 것부터 먼저 넣는다.
        heapq.heappush(heap, i)
while heap:
    num = heapq.heappop(heap)  # 선행문제 없이 풀어도 되는 문제 중 숫자가 낮은 것부터 heappop으로 꺼낸다.
    result.append(num)
    for i in arr[num]:
        # 해당 선행문제를 풀었을 때 풀 수 있는 문제들 확인
        precede[i] -= 1
        # 더 이상 선행문제가 없으면 0이 됨. 그러면 해당 문제를 heap에 넣는다.
        if precede[i] == 0:
            heapq.heappush(heap, i)
print(*result)