def solution(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    elif a%2 == 0 or b%2 == 0 :
        return 2*(a+b)
    else:
        return (a**2+b**2)