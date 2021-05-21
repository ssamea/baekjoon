n=int(input())

for i in range(1,n+1):
    stack=list(input().rstrip().split())
    print("Case #%d: %s" %(i, ' '.join(stack[::-1])))


