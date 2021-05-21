#각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량
#모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
#각각의 로프에는 모두 고르게 중량이 걸림
#로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성

n=int(input())
loop=[]

for i in range(n):
    weight=int(input())
    loop.append(weight)

temp= 0
loop.sort(reverse=True)

for i in range(n):
    loop[i]=loop[i]*(i+1)
    temp=max(loop)

print(temp)
