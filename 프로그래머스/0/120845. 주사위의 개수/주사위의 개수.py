def solution(box, n):
    answer = 0
    
    for i in box:
        answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer