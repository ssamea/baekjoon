#나이순 정렬
# 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

import sys
sys.setrecursionlimit(10000)

n=int(sys.stdin.readline())
list=[]

for _ in range(n):
    age,name=map(str, input().split())
    age=int(age)
    list.append((age,name))

list.sort(key=lambda x:(x[0]))

for x in range(n):
    print(list[x][0],list[x][1])