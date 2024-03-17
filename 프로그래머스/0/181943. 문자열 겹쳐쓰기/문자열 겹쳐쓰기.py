def solution(my_string, overwrite_string, s):
    len_overwrite = len(overwrite_string)
    # answer = my_string.replace(my_string[s:len_overwrite+s],overwrite_string)
    
    answer = my_string[:s] + overwrite_string + my_string[s+len_overwrite:]
    print(my_string[:s])
    print(overwrite_string)
    print(my_string[s+len_overwrite:])
    return answer