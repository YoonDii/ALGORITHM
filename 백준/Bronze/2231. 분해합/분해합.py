n = int(input())

for i in range(n):            # 범위는 n 내에서
    m = sum(map(int, str(i))) # i를 문자열로 변환하여 값을 더함.
    result = i + m            # result는 i와 m을 합한값으로 초기화.  
    if result == n:           # result값이 n과 같으면 i는 생성자라서 출력
        print(i)
        break
else:                         # 생성자가 없으면 0을 출력
    print(0)