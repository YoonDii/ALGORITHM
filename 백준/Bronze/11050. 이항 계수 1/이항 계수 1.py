from math import factorial #이항계수가 뭔지 알아야한다. 이항계수를 구하는 공식 b로 풀면됨! 사용함수는 팩토리얼
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)