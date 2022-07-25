def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for x in range(i+1,len(numbers)):
            if numbers[i] + numbers[x] != answer:
                answer.add(numbers[i]+ numbers[x])
    answer = list(answer)
    answer.sort()
    return answer