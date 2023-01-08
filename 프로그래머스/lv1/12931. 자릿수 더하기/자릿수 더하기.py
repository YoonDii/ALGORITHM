def solution(n):
    answer = 0
    nums = list(map(int,str(n)))
    # print(nums)[1, 2, 3]
    for i in range(len(nums)):
        answer += nums[i]
    return answer