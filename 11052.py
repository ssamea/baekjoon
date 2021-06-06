n=int(input())
arr= [0]+list(map(int,input().split()))

dp=[0]*(n+1)
dp[1] = arr[1]
dp[2] = max(dp[0]+arr[2], dp[1]+arr[1])

for i in range(3, n+1):
    dp[i] = arr[i]  # 자기 자신
    for j in range(1, i- 1):
        dp[i]=max(dp[i], dp[j]+dp[i-j])

print(dp[n])