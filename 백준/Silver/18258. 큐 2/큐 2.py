import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque() #빼야할게 많을 때는 deque!

for i in range(n):
    rule = list(map(str,sys.stdin.readline().split()))

    if rule[0] == 'push': # push면 queue에 넣기
        q.append(int(rule[1]))
    
    elif rule[0] == 'pop': #pop이면 큐가 아니면 -1출력/ 맞으면 맨처음꺼 빼고 뺀 수 출력
        if q:
            print(q.popleft())
        else:
            print('-1')
        
    elif rule[0] == 'size':#size면 정수의 개수 출력/ 큐 길이재기
        print(len(q))
    
    elif rule[0] == 'empty': #empty면 큐가 비어있으면 -1출력/큐가 있으면 0출력
        if len(q) == 0:
            print('1')
        else:
            print('0')

    elif rule[0] == 'front': #front면 큐가비어있으면 -1출력/아니면 제일앞에있는 수 출력
        if q:
            print(q[0])
        else:
            print('-1')

    elif rule[0] == 'back':#back이면 큐가 비어있으면 -1출력/ 아니면 가장마지막수 출력
        if q:
            print(q[-1])
        else:
            print('-1')