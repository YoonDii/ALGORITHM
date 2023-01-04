
t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # print(arr)[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    x, y, cnt, dr = 0, 0, 1, 0  # 초기값 // cnt가 1인 이유는 1부터 시작해서
    arr[x][y] = cnt
    cnt += 1  # 숫자가 증가하니까 cnt도 증가

    while cnt <= n * n:
        nx, ny = x + dx[dr], y + dy[dr]  # 다음좌표는 현재좌표+방향

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            # 조건에 맞으면 다음좌표로 넘어가기
            x, y = nx, ny
            arr[x][y] = cnt
            cnt += 1
        else:
            dr = (dr + 1) % 4  # 방향도 바꾸는데 인덱스는 3까지여서 4부터는 0으로 되돌아가게 하기
    print(f"#{tc}")
    for i in arr:
        print(*i)