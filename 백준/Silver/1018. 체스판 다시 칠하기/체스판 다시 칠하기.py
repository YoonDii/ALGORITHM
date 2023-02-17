n, m = map(int, input().split())  # 보드의 크기 입력받기
board = [input() for _ in range(n)]  # 보드의 상태 입력받기

min_count = n * m  # 최소값을 구하기 위한 초기값 설정

# 모든 경우에 대하여 다시 칠해야 하는 정사각형 개수 계산하기
for i in range(n - 7):
    for j in range(m - 7):
        count = 0  # 다시 칠해야 하는 정사각형 개수
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 체스판과 다른 색이면 count 증가
                if (x + y) % 2 == 0:  # (0, 0)이 흰색인 경우
                    if board[x][y] != 'W':
                        count += 1
                else:  # (0, 0)이 검은색인 경우
                    if board[x][y] != 'B':
                        count += 1
        count = min(count, 64 - count)  # 반대로 칠하는 경우 고려
        min_count = min(min_count, count)

print(min_count)  # 결과 출력
