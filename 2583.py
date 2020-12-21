import sys

sys.setrecursionlimit(50000)

M, N, K = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(M + 1)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(arr, i, j):
    cnt = 1
    for k in range(4):
        i_ = i + dx[k]
        j_ = j + dy[k]
        if 0 <= i_ < M and 0 <= j_ < N:
            if arr[i_][j_] == 0:
                arr[i_][j_] = -1
                cnt += dfs(arr, i_, j_)
    return cnt


for k in range(K):
    uX_, uY, tX, tY = map(int, input().split())
    while uY < tY:
        uX = uX_
        while uX < tX:
            arr[M - 1 - uY][uX] = 1
            uX += 1
        uY += 1

square = 0
answer = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = -1
            answer.append(dfs(arr, i, j))
            square += 1

print(square)
answer.sort()
for i in range(len(answer)):
    print(answer[i], end=' ')