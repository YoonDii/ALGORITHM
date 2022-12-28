def solution(s):
    stack = []
    for num in s.split():
        try:
            stack.append(int(num))
        except:
            if stack:
                stack.pop()
    return sum(stack)