#단어 수학
#첫째 줄에 단어의 개수 N
#둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다.

n=int(input())
arr= []

for i in range(n):
    arr.append(input())  # n만큼 한줄 씩 입력

alphabet = [0 for i in range(26)]

res=0

for i in arr:
    cnt=0
    while i:
        now= i[-1]
        alphabet[ord(now) - ord('A')] += pow(10, cnt)
        cnt+=1
        i=i[:-1]

alphabet.sort(reverse=True)

for i in range(9,0,-1):
    res+=i*alphabet[9-i]
print(res)