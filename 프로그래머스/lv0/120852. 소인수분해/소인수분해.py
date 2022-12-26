def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n /= i
        else:
            i += 1

    return list(sorted(set(answer)))