# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
for tc in range(1,11):
    n, nums = (input().split())
    
    pw = [] #이걸 스택이라고 생각
    for i in nums: # pw이 비어있지 않고, pw의 마지막 글자와 i와 같다면 중복이므로 pop으로 삭제
        if pw and i == pw[-1]:
            pw.pop()
        else:
            pw.append(i)
    print('#{} {}'.format(tc, ''.join(pw))) #join함수는 하나씩들어온 리스트의 매개변수를 문자열로 합쳐서 반환해주는 함수