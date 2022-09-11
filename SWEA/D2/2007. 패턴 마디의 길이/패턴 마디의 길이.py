# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

for i in range(int(input())):
    s=input()
    for j in range(1,10):
        if s[:j]==s[j:2*j]:
            print(f'#{i+1} {j}')
            break