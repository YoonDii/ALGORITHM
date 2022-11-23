def solution(array):
    ans = [0] * 1001
    for i in array:
        ans[i] += 1
    mx = max(ans)
    
    num = 0
    for i in ans:
        if mx == i :
            num += 1
    if num == 1 :
        return ans.index(mx)
    else:
        return -1
