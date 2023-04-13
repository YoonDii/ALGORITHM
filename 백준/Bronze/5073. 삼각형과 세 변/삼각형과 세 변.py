import sys
input = sys.stdin.readline

while True:
    # 입력
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    # 삼각형 판별
    if a == b == c:
        print("Equilateral")
    elif 2 * max(a, b, c) >= a + b + c:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")