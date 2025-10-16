def solution(slice, n):
    answer = n//slice
    if n%slice >0:
        answer +=1
    return answer

print(solution(7,10))
print(solution(4,12))