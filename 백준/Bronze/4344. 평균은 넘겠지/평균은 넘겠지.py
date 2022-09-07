c = int(input())

for i in range(c):
    data = list(map(int, input().split()))  # 일단 다 리스트로 받아주고
    # 제일 처음이 인원이고, 1번째부터 마지막까지가 점수라서 더해준다. 평균구하기~
    avg = sum(data[1:]) / data[0]
    count = 0  # 평균을 넘는 사람을 세야하기 때문에 0으로 초기화

    for i in range(1, len(data)):
        if data[i] > avg:  # 점수가 평균을 넘으면 카운트하기
            count += 1

    result = count / data[0] * 100  # 평균넘는 학생들 비율구하기
    print('%.3f' % result+'%')  # 출력이 반올림하여 소수점 셋째자리까지 출력