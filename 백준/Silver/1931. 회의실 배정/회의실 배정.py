from heapq import heappop,heappush

n = int(input())

times = []
for i in range(n):
    start , end = map(int,input().split())
    heappush(times,(end,start)) # 끝시간과 시작시간을 정렬한다.


cnt = 0
answer = 0

while times :
    a, b = heappop(times) # 하나씩 빼면서 비교하기
    if b >= cnt: # b가 cnt보다 크면
        cnt = a # a와 cnt가 같다   
        answer += 1
print(answer)

'''
(4,1) (5,3) (6,0) (7,5)가 있으면
a,b = (4,1)
if 1 >= cnt : 지금은 cnt가 0이기때문에
    cnt = 4
    answer에 1을 더함 
    
    b가 cnt보다 계속 크면 answer가 1씩 증가해서 회의실 개수 알수있음
'''
