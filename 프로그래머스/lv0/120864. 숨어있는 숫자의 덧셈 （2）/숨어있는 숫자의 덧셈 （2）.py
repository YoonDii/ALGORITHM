import re

def solution(my_string):
    numbers = list(map(int,re.findall(r'\d+', my_string)))
    # \d는 숫자를 한 글자만 찾는다.
    # +는 '하나 혹은 그 이상 연결된' 이란 뜻이다.
    # 즉, \d+는 '하나 혹은 그 이상 연결된 숫자`이다.
    return sum(numbers)