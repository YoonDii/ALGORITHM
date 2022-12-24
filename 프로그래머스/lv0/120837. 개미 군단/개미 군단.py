def solution(hp):
    a = hp // 5 #장군개미 수
    b = (hp -(a*5))// 3 #장군개미수를 계산 후 남은 수로 병정개미 수 구하기
    c = (hp-(a*5)-(b*3)) // 1 #일개미 수 구하기
    
    return a + b + c
    
    