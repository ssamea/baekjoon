import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from bisect import bisect_left,bisect_right

def binary_search(arr, target, start, end):#a,left,right
    """
    a.sort()
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index
    """
    arr.sort()
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] > target:  # 탐색 값이 기준점보다 작다면
            end = mid - 1

        elif  arr[mid] == target:
            return True

        else:  # 탐색 값이 기준점보다 크다면
            start = mid + 1


n = int(input())
a = list(map(int,input().split()))

m = int(input())
target = list(map(int,input().split()))


for i in range(m):
    if binary_search(a, target[i], 0, n-1):
        print(1)
    else:
        print(0)

