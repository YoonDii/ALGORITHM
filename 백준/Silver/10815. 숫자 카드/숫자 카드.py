n = int(input())
nn = sorted(list(map(int, input().split())))  # 중앙값구하는 리스트/ 꼭 정렬해주기!

m = int(input())
mm = list(map(int, input().split()))  # 타겟이 되는 리스트

for i in range(m):
    find = False
    target = mm[i]  # m만큼 돌면서 타겟 확인하기

    start = 0
    end = len(nn) - 1  # 인덱스로 봐야하기때문에 -1 / 인덱스 0~n-1까지

    while start <= end:
        midx = int(start + end) // 2  # 중앙값인덱스
        mid = nn[midx]  # 중앙값

        if mid > target:
            end = midx - 1  # 중앙값이 타겟보다 크면 중앙값이 더 작아지게 인덱스를 줄여줌(중앙값오른쪽은 볼필요가없다는말)
        elif mid < target:
            start = midx + 1  # 중앙값이 타겟보다 작으면 중앙값이 더 커지게 인덱스를 키워줌(중앙값왼쪽은 볼필요가없다는말)
        else:
            find = True  # 중앙값과 타겟이 값으면 찾음, 반복문 종료
            break

    if find:  # 찾았으면 1출력/ 아니면 0출력
        print(1, end=" ")
    else:
        print(0, end=" ")
