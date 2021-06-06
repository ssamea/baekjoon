# 연속합
#  연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합

n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 입력
dp = [0]*100001
result = -1001

for i in range(n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    result = max(result, dp[i])

print(result)

