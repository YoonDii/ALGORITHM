def solution(my_string, s, e):
    print(my_string[:s])
    print(''.join(reversed(my_string[s:e])))
    print(my_string[e+1::])
    return my_string[:s]+ ''.join(reversed(my_string[s:e+1]))+ my_string[e+1::]