def solution(phone_number):
    secret = len(phone_number)-4 # 뒷4자리 빼기
    result = secret * "*" + phone_number[-4:] #비밀과 뒷자리합치기
    # print(phone_number[-4:]) 4444
    return result
    
    