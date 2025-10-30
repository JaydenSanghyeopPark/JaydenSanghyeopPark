def solution(array, n):
    array.sort()
    answer = []
    
    for i in array:
        answer.append(abs(i-n))
    m=min(answer)
    f=answer.index(m)
    return array[f]