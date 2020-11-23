#잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
#1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수

n=int(input())
change=1000-n # n=380 -> change= 620
cnt=0

while(True):
    if change==0:
        break

    else:
        if change // 500 != 0:
            cnt += change // 500
            change %= 500


        elif change // 100 !=0:
            cnt += change // 100
            change %= 100


        elif change // 50 != 0:
            cnt += change // 50
            change %= 50


        elif change // 10 != 0:
            cnt += change // 10
            change %= 10


        elif change // 5 != 0:
            cnt += change // 5
            change %= 5


        else :
            cnt += change // 1
            change %= 1


print(cnt)