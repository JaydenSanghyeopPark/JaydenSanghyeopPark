def solution(spell, dic):
    answer = 2
    
    for d in dic:
        if set(spell) == set(d):
            answer = 1
            break
    return answer

        