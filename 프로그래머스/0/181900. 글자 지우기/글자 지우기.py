# def solution(my_string, indices):
#     for i in range(0,len(my_string)-1):
#         if i == int(indices[i]-1):
#             my_string.remove(my_string[i])

#     return my_string

def solution(my_string, indices):
    # 문자열을 리스트로 변환
    my_list = list(my_string)
    
    # indices를 내림차순 정렬
    indices.sort(reverse=True)
    
    # 각 인덱스에 해당하는 문자 제거
    for index in indices:
        if 0 <= index < len(my_list):  # 인덱스 범위 확인
            my_list.pop(index)
    
    # 리스트를 다시 문자열로 변환
    return ''.join(my_list)
