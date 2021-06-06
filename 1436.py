# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
n = int(input())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1