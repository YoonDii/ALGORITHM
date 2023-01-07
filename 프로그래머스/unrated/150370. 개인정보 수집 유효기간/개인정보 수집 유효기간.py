def solution(today, terms, privacies):
    dic = {}
    today = map(int, today.split("."))
    year, month, day = today  # today의 요소가 3개이기 떄문에 값이 나옴
    # print(year, month, day)2022 5 19

    for i in terms:
        i = i.split(" ")
        dic[i[0]] = int(i[1])
    # print(dic){'A': 6, 'B': 12, 'C': 3}

    cnt = 1
    result = []
    for j in privacies:
        days, grade = j.split(" ")
        y, m, d = map(int, days.split("."))
        m += dic[grade]

        while m > 12: #제한사항에 유효기간은 1이상100이하여서 while로 돌려주기
            y += 1
            m -= 12

        if year > y:
            result.append(cnt)
        elif year == y:
            if month > m:
                result.append(cnt)
            elif month == m:
                if d <= day:
                    result.append(cnt)
        cnt += 1
    return(result)