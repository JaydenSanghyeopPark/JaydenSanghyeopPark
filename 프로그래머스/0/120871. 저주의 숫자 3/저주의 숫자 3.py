def solution(n):
    answer = 0
    
    for _ in range(n):
        answer += 1
        
        for i in range(n):
            if answer % 3 == 0 or '3' in str(answer):
                answer += 1
    return answer