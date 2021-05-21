# 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다. 기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다.
# 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다.
# 각 도시에는 단 하나의 주유소가 있으며, 도시 마다 주유소의 리터당 가격은 다를 수 있다.
# 가격의 단위는 원을 사용한다.

n=int(input())
dist=list(map(int,input().split())) # 두 도시를 연결하는 도로의 길이
cost=list(map(int,input().split())) # 주유소의 리터당 가격
res=0
min_cost=cost[0]



# 왼쪽이나 오른쪽 최소값을 구하려면 순방향, 역방향을 순차적으로 방문함

for i in range(n-1):
    if min_cost > cost[i]:
        min_cost=cost[i]
    res+= dist[i]*min_cost

print(res)