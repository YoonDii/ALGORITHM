# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()  # 시간정렬

    ans = "Possible"
    for i in range(n):
        # customer시간까지 만들어진 붕어 개수 (customer // m) * k . i+1해주는 이유는 인당 1개씩 구매하기때문.
        pang = (customer[i] // m) * k - (i+1)

        if pang < 0:  # 만약 빵이 0보다 작으면 없어서 못팜
            ans = "Impossible"
            break

    print(f'#{tc} {ans}')