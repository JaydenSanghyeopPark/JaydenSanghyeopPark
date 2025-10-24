def solution(i, j, k):
    answer = 0
    k = str(k)
    
    for l in range(i, j+1):
        answer += str(l).count(k)
    
    return answer