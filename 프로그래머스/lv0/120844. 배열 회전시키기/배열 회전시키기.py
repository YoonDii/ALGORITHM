from collections import deque
def solution(numbers, direction):
    answer = []
    q = deque(numbers)
    if direction ==  'right':
        q.rotate(1)
    else:
        q.rotate(-1)
    for i in q:
        answer.append(i)

    return answer