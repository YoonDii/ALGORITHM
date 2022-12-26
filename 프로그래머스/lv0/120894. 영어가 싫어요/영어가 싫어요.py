def solution(numbers):
    nums = ["zero",'one','two','three','four','five','six','seven','eight','nine']
    
    for index,num in enumerate(nums):
        #enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple) 을 만들어줌
        numbers = numbers.replace(num,str(index))
    return int(numbers)