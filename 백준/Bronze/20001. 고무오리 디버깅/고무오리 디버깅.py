stack = []
 
while True:
    s = input()
    if s == '문제':
        stack.append(1)
    elif s == '고무오리': #
        if not stack: # 풀문제가 없다면 문제를 추가한다
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()
    elif s == '고무오리 디버깅 끝':
        break
 
if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')