def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        #a = 2진수로 바꾸고 앞에 0b를 지우고 
        #문자열의 왼쪽에 0을 추가하여 전체 길이가 n이 되도록 한다.
        a = bin(arr1[i] | arr2[i])[2:].zfill(n)
        #b =1은#으로 바꾸고, 0은 공백으로 바꾼다.
        b = a.replace("1", "#").replace("0", " ")
        answer.append(b)
    return answer