import itertools
n, k = map(int,input().split())
arr = []
dp = [0]*(k+1)

dp[0] = 1 # 자기 자신일 때, 즉, 1원일때 1원만 사용하는겨우, 2원일 때 2원만 사용하는경우, 3원일 때 3원만 사용하는경우

for _ in range(n):
    arr.append(int(input()))

for i in arr:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])
