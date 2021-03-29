#숫자 카드
import sys
sys.setrecursionlimit(10000)

n=int(input())
a=list(map(int,input().split()))

m=int(input())
b=list(map(int,input().split()))

a.sort()


for i in range(m):
    if b[i] in a:
        print(1, end=' ')
    else:
        print(0, end=' ')

