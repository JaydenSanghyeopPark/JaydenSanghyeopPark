def solution(n):
    answer = n//7
    if n%7 >0:
        answer +=1
    return answer
print(solution(7))
print(solution(1))
print(solution(15))