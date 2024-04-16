def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower()== True:
            answer+=i.upper()
        elif i.isupper()==True:
            answer+=i.lower()
    return answer