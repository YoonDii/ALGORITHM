def solution(s):
#     answer = True
    
#     for i in range(len(s)):
#         if s[0] == s[-1]:
#             return False
#         elif s[0] ==')'and s[-1] =='(':
#             return False
#     return True

    stk = []
    
    for i in s:
        if i == '(':
            stk.append('(')
        else:
            if stk == []:
                return False
            else:
                stk.pop()
    if stk != []:
        return False
    return True