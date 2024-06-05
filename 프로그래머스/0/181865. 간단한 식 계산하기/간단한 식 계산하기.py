def solution(binomial):
    a, op, b = binomial.split()   
    
    if op == '+': return int(a) + int(b)    
    if op == '-': return int(a) - int(b)    
    if op == '*': return int(a) * int(b)    
    if op == '/': return int(a) / int(b)
    
