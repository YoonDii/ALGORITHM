t = int(input())

for tc in range(1, t + 1):
    s = list(input())
    ss = list(set(s))  # 중복제거

    check = True
    for i in ss:
        if s.count(i) != 2:
            check = False
    if check:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")