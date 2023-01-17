def solution(n, m):
    gcd = 1 #최대공약수
    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    lcm = n * m // gcd #최소공배수 구하기
    answer = [gcd, lcm]
    return answer