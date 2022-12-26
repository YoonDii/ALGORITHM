# def solution(before, after):
#     list_before = list(before)
#     # print(list_before)['o', 'l', 'l', 'e', 'h']
#     list_after = list(after)
#     # print(list_after)['h', 'e', 'l', 'l', 'o']
#     if list_before[::-1] == list_after:
#         return 1
#     else:
#         return 0


def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
        
  