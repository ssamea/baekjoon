#1, 2, 3 더하기
# 수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 다이나믹= 중복 횟수를 최소화 하는 것

n= int(input())

data=[]

for i in range(n):
   data.append(int(input())) #n만큼 한줄 씩 입력


d=[0]*11 #메모리제이션 최대갯수

def dn(x):
    if x==1:
        return 1
    if x==2:
        return 2
    if x==3:
        return 4

    d[x]=dn(x-1)+dn(x-2)+dn(x-3)
    return d[x]

for i in data:
    res=dn(i)
    print(res)

