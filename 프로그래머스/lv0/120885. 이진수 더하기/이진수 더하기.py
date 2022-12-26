def solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2,2)
    answer = bin(a+b)
    return answer.replace("0b","")
#그대로 출력하게 되면 아래와 같은 화면처럼 2진수를 뜻하는 "0b"가 붙어서 나오기 때문에 0b를 없애준다