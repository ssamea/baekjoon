data=input().split('-') #가장 처음과 마지막 문자는 숫자 50 - (30 + 40)
res=0

for i in data[0].split('+'):
    res+=int(i)

for i in data[1:] :
    for j in i.split('+'):
        res-=int(j)

print(res)