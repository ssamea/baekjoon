# 균형잡힌 세상
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

while True:
    str=input() # 문자열을 받을 때마다 스택에 넣자
    stack=[]
    res=True

    if str== ".": #.이면 입력 받기 끝
        break

    for i in str:
        if i == "(" or i == "[":
            stack.append(i)

        elif i ==")":  #오른쪽 괄호가 먼저 나온경우는 false, 짝을 이룬경우는 True 를 출력하도록 놔눠야함
            if len(stack)==0: #오른쪽 소괄호가 앞에 먼저 나올 경우
                res=False
                break

            if stack[-1]=="(":
                stack.pop()

            else:
                answer = False
                break

        elif i == "]":  # 오른쪽 괄호가 먼저 나온경우는 false, 짝을 이룬경우는 True 를 출력하도록 놔눠야함
            if len(stack) == 0:  # 오른쪽 소괄호가 앞에 먼저 나올 경우
                res = False
                break

            if stack[-1] == "[":
                stack.pop()

            else:
                answer = False
                break

    if res and not stack:
          print("yes")

    else:
          print("no")


