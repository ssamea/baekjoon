#좌표 정렬하기 2

import sys
sys.setrecursionlimit(10000)

n=int(input())
list=[]

for _ in range(n):
    x,y=map(int, input().split())
    list.append((x,y))

list.sort(key=lambda y:(y[1]))

for y in range(n):
    print(list[y][0], list[y][1])