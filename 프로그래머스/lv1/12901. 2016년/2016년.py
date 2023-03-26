#이 방법은 테케3,4,에서 런타임에러가 난다.
# import datetime
# def solution(a, b):
#     answer = 'MON TUE WED THU FRI SAT'.split()
#     return answer[datetime.datetime(2016,a,b).weekday()]

def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI',"SAT",'SUN','MON',"TUE",'WED','THU']
    temp = 0
    answer = ''
    if a == 1:
        temp = b % 7
        answer = weeks[temp-1]
    else :
        for i in range(a-1) :
            temp += days[i]
        temp +=b
        temp %= 7
        answer = weeks[temp-1]

    return answer
    
