def solution(dots):
    x = []
    y = []
    
    for d in dots:
        x.append(d[0])
        y.append(d[1])
    
    a = max(x) - min(x)
    b = max(y) - min(y)
    
    return a*b