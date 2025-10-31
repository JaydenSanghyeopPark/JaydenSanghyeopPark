def solution(num_list):
    j=0
    v=0
    for i in num_list:
        if i % 2 == 0:
            j += 1
        else:
            v += 1
    answer = [j,v]
    
    return answer