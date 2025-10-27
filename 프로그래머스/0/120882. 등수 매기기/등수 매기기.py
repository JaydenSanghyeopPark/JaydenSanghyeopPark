def solution(score):
    avg = []
    
    for i in score:
        avg.append(sum(i)/2)
        
    s_avg = sorted(avg, reverse=True)
    
    answer = []
    
    for j in avg:
        answer.append(s_avg.index(j) + 1)
    
    return answer
    
    