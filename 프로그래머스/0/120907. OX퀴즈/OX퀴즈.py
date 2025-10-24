def solution(quiz):
    answer = []
    
    for i in quiz:
        a = i.split(" ")
        
        num1 = int(a[0])
        num2 = int(a[2])
        num3 = int(a[4])
        
        if a[1] == "+":
            result = num1 + num2 == num3
            answer.append("O" if result else "X")
        else:
            result = num1 - num2 == num3
            answer.append("O" if result else "X")
    return answer