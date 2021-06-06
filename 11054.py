# 바이토닉 수열 : S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN
n=int(input())
arr=list(map(int,input().split()))
dpi = [1]*n  # 증가하는 수열
dpd= [1]*n  # 감소하는 수열
ans=[0]*n  #결과

# 증가 부분과 감소 부분을 나눈다 최장수열 느낌
# 증가 부분 순차 탐색
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dpi[i] = max(dpi[i], dpi[j]+1)


# 감소하는 부분
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dpd[i] = max(dpd[i], dpd[j]+1)

for i in range(n):
    ans[i]=dpi[i]+dpd[i]-1  # 두 리스트의 합을 구한 후 두 리스트의 합에서 가장 큰 값은 실제 길이를 구할 때에는 중복되어 더해지기 때문에 1을 빼주면 된다.

print(max(ans))
