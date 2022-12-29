n = int(input())
stack = []

for i in range(n):
    num = int(input())
    if num == 0:
        stack.pop()  # 맨위 숫자를 뺀다
    else:
        stack.append(num)  # 숫자 넣기

print(sum(stack))