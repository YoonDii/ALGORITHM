sent = input()
bomb = list(input())

stack = []

for i in range(len(sent)):
    stack.append(sent[i])  # 문자열 하나씩 추가
    if stack[-len(bomb) :] == bomb:  # 스택의 마지막이 bomb 문자열과 같으면
        del stack[-len(bomb) :]  # 스택의 마지막 삭제

if stack:
    print("".join(stack))
else:
    print("FRULA")
