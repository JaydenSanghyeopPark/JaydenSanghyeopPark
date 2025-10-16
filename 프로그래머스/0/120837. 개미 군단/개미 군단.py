def solution(hp):
    #a는 장군개미, b는 병정개미, c는 일개미
    a=hp//5
    d=hp%5
    b=d//3
    c=d%3
    return a+b+c

print(solution(23))
print(solution(24))
print(solution(999))
