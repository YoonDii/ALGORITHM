def solution(my_string):
    moum = ("a,e,i,o,u")
    for i in moum :
        my_string = my_string.replace(i,"")
    return my_string