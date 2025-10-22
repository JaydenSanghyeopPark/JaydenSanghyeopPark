def solution(my_string):
    low=my_string.lower()
    sort=sorted(low)
    answer = "".join(sort)
    return answer