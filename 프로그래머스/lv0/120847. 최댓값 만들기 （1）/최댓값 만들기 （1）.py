def solution(numbers):
    s_numbers = sorted(numbers)
    # print(s_numbers) [0, 1, 9, 10, 24, 31]
    return (s_numbers[-1]*s_numbers[-2])
    
   