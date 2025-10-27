def solution(num, total):
    s= total/num - ((num-1)/2)
    
    answer = []
    for i in range(num):
        answer.append(s)
        s += 1
        
    return answer