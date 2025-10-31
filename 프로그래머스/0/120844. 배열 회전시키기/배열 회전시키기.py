def solution(numbers, direction):
    result = []
    if direction == 'right':
        result = numbers[-1:] + numbers[:-1]
    else:
        result = numbers[1:] + numbers[:1]
    return result
