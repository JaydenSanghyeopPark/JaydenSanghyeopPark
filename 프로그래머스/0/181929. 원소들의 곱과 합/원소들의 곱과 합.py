def solution(num_list):
    s = sum(num_list) **2
    product = 1
    for m in num_list:
        product *= m
        
    if product < s:
        return 1
    else:
        return 0