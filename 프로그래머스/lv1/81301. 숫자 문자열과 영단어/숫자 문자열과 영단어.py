def solution(s):
    ans = s

    words  = {
        'zero':0, 'one':1, 'two':2, 'three':3,
        'four':4, 'five':5, 'six':6, 'seven':7,
        'eight':8, 'nine':9
    }


    for item in words.items():
            ans = ans.replace(item[0], str(item[1])) 
    
    return int(ans)