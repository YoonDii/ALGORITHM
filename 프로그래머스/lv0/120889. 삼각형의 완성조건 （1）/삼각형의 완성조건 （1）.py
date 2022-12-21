def solution(sides):
    s_sides = sorted(sides)
    # print(s_sides)
    max_s = max(sides)
    # print(max_s)
    if s_sides[0] + s_sides[1] > max_s:
        return 1
    else :
        return 2
    
    