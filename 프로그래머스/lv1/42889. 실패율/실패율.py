def solution(N, stages):
    result = {}
    game = len(stages)
    for i in range(1,N+1):
        if game != 0:
            cnt = stages.count(i)
            result[i] = cnt / game
            game -= cnt
        else:
            result[i] = 0
    return sorted(result,key=lambda x : result[x], reverse=True)