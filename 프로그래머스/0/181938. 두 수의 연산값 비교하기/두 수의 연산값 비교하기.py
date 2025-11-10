def solution(a, b):
    answer = 0
    num1 = str(a) + str(b)
    num2 = 2*a*b
    
    if int(num1) >= num2:
        return int(num1)
    else:
        return num2
