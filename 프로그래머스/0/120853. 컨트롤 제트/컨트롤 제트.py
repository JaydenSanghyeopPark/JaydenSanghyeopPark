def solution(s):
    v = []
    stack = s.split()
    for i in stack:
        if i == 'Z':
            if v:
                v.pop()
        else:
            v.append(int(i))
            
    return sum(v)