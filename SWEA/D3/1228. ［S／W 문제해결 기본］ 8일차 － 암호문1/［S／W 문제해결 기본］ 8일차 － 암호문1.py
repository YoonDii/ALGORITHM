
for tc in range(1,11):
    n = int(input()) # 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
    nums = list(map(int,input().split())) # 두 번째 줄 : 원본 암호문
    rn = int(input()) # 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
    qus = list(input().split()) # 네 번째 줄 : 명령어 /문자랑 숫자랑 같이 있기 때문에 문자열로 받아줌.

    for i in range(len(qus)):
        if qus[i] == "I": # I라면 x는 명령어에서 I 다음의 수, y는 x다음의 수
            x = int(qus[i+1])
            y = int(qus[i+2])

            for j in range(y):
                nums.insert(x+j, int(qus[i+2+(j+1)]))

    print("#{} {} {} {} {} {} {} {} {} {} {}".format(tc, *nums[0:10])) # 10개만 출력해야됨

