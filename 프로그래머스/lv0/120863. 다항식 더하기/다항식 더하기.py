def solution(polynomial):
    polynomial = polynomial.replace(' ', '').split('+')
    print(polynomial)
    x = 0
    num = 0
    for i in polynomial:
        if 'x' in i:
            if i == 'x':
                x += 1
            else:
                x += int(i[:-1])
        else:
            num += int(i)
            
    answer = ''
    if x:
        if x == 1:
            answer += 'x'
        else:
            answer += str(x)+'x'
    if num:
        if x:
            answer += ' + '
        answer += str(num)
    return answer

    