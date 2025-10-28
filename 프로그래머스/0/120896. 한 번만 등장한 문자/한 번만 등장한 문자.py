def solution(s):
    char_counts={}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    single_chars = []
    for char, count in char_counts.items():
        if count == 1:
            single_chars.append(char)
    return "".join(sorted(single_chars))