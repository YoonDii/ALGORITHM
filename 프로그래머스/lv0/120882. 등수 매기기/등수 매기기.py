# def solution(score):
    # english = [jumsu[0] for jumsu in score]
    # math = [jumsu[1] for jumsu in score]
    # result = (english + math) // 2
    # print(result)
    
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    # print(a)	[150, 140, 130, 110]
    return [a.index(sum(i))+1 for i in score]
    