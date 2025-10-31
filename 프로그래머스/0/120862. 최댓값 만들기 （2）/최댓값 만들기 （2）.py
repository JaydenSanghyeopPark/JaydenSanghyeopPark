def solution(numbers):
    numbers.sort()
    
    plus = numbers[0]*numbers[1]
    minus = numbers[-1]*numbers[-2]
    
    if plus > minus:
        return plus
    else:
        return minus