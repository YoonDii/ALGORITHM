# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0 for x in range(bridge_length)]
    
#     while bridge:
#         answer += 1
#         bridge.pop(0)
        
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 ans = truck_weights.pop(0)
#                 bridge.append(ans)
#             else:
#                 bridge.append(0)
                
#     return answer 시간초과 나와서 실패

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = deque([0] * bridge_length)  # 다리를 deque로 변경
#     truck_weights = deque(truck_weights)  # 트럭 목록도 deque로 변경
    
#     while bridge:
#         answer += 1
#         bridge.popleft()  # deque 의 popleft() 사용
        
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 bridge.append(truck_weights.popleft())
#             else:
#                 bridge.append(0)
#         elif not any(bridge):  # 다리 위에 트럭이 없으면 반복 종료
#             break
                
#     return answer

def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가  
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time