import heapq
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    # 전화번호부를 정렬한 후에 현재 번호와 그 다음 번호의
    # 접두사 여부만 보면 된다.
    # 문자열을 정렬할 경우 앞에 오는 숫자/문자가 작으면 길이에 상관 없이 무조건 작은 것으로 간주
    # 만일 앞 문자가 같을 경우 뒤 문자를 비교하는데, 혹 뒤 문자가 없는 것이 있으면 그것이 작은 것
    # sorting을 해서 할 수도 있지만 그냥 힙을 쓰기로 했다.
    #phone_book.sort(key=lambda x:len(x))
    heapq.heapify(phone_book)
    answer = True
    p_num = heapq.heappop(phone_book)
    while phone_book:
        i = len(p_num)
        # slicing은 범위를 벗어나도 있는 만큼만 출력하므로 no error, index와 다름
        if p_num == phone_book[0][:i]:
            return False
        p_num = heapq.heappop(phone_book)

    return answer

