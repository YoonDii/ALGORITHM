def solution(lottos, win_nums):
    # lottos: [44, 1, 0, 0, 31, 25]
    # win_nums: [31, 10, 45, 1, 6, 19]

    zeros = lottos.count(0)               # 리스트에서 0의 개수 세기
    win = 0                               # win 변수 = 맞춘 개수 (0으로 초기화)
    scores = {0: 6, 1: 6, 2: 5, 3: 4,     # ★ 포인트1. 경우의 수가 7개 밖에 없으므로
              4: 3, 5: 2, 6: 1}           #           각각의 맞춘 개수에 순위 할당하기
                                          # ★ 포인트2. 0개 맞은 순위 = 1개 맞은 순위
    
    for l in lottos:                    
        if l in win_nums:
            win += 1
    
    most = win + zeros                    # 맞춘 번호 + 0이 다 맞았다고 가정 -> 최고 순위
    least = win                           # 0이 다 틀렸다고 가정 -> 최저 순위
    return [scores[most], scores[least]]  # 딕셔너리를 이용하여 깔끔하게 리턴