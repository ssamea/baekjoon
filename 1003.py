
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력

t = int(input())
cnt1=[1,0]
cnt2=[0,1]

for i in range(t):
    n = int(input())

    for i in range(2, 41):
        cnt1.append(cnt1[i-1]+cnt1[i-2])
        cnt2.append(cnt2[i - 1] + cnt2[i - 2])

    print("%d %d" % (cnt1[n], cnt2[n]))
    #cnt1,cnt2=0,0

