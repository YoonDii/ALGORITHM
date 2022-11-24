x = int(input())
count = 0
n = 64
while x > 0:
    if n > x:
        n = n // 2  # x보다 크면 반으로 자르기
    else:
        count += 1  # 막대기 갯수세기
        x -= n  # x보다 작은지 확인
print(count)
