def solution(my_string, n):
    answer = ''
    
    string=list(my_string)
    for i in range(0,len(string)):
         string[i] = string[i] * n
    answer = ''.join(string)
    return answer