for i in range(int(input())):
    a, b = input().split()
    li = []
    for x in range(len(a)):
        if ord(a[x]) > ord(b[x]):  # ord는 문자를 유니코드 정수로 반환하는 함수
            li.append(26 - (ord(a[x]) - ord(b[x])))
        else:
            li.append(ord(b[x]) - ord(a[x]))
    print("Distances:", *li)
