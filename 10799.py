#쇠막대기
#레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
#쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.

bar=list(input())
cnt=0
stack=[]

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')

    else:
        if bar[i-1] == '(':
            stack.pop()
            cnt+=len(stack)

        else:
            stack.pop()
            cnt+=1
print(cnt)