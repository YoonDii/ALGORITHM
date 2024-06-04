def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        ans = []
        
        for i in range(s,e+1):
            if arr[i] > k:
                ans.append(arr[i])
        if ans:
            answer.append(min(ans))
        else:
            answer.append(-1)
    return answer