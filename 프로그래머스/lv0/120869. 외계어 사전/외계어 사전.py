def solution(spell, dic):
    spell = set(spell) 
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2