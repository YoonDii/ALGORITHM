t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))

    # (중요도, 인덱스) 쌍으로 변환하여 대기열로 유지
    queue = [(docs[i], i) for i in range(n)]

    # 출력 순서
    order = 0

    while queue:
        doc = queue.pop(0)
        if any(doc[0] < q[0] for q in queue):
            # 현재 문서가 대기열에서 우선순위가 가장 높지 않다면, 대기열의 뒤쪽에 추가
            queue.append(doc)
        else:
            # 현재 문서가 대기열에서 우선순위가 가장 높다면, 출력 순서를 1 증가
            order += 1
            if doc[1] == m:
                # 출력 순서가 찾고자 하는 문서의 순서와 같다면, 출력 순서를 출력하고 종료
                print(order)
                break
