def solution(n):
    answer = []
    
    for n in str(n):
        answer.append(int(n))
    answer = sum(answer)
    
    return answer