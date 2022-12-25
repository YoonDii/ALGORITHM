def solution(numbers):
    numbers.sort()
    print(numbers)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    