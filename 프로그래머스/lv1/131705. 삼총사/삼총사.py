from itertools import combinations

def solution(number):    
    num_combinations = [sum(comb) for comb in list(combinations(number, 3)) if sum(comb) == 0]
    
    return len(num_combinations)