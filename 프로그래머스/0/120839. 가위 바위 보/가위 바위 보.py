def solution(rsp):
    answer = ""
    for r in rsp:
        if r == "2":
            answer += "0"
        if r == "0":
            answer += "5"
        if r == "5":
            answer +="2"
            
    return answer