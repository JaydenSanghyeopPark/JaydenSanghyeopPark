def solution(n):
    answer = 0
    
    for i in range(n+1):
        v = 0
        for j in range(1, i+1):
            if i % j == 0:
                v += 1
        if v >= 3:
            answer += 1    
            
    return answer