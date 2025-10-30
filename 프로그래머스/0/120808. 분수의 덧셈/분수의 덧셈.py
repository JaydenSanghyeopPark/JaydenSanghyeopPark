import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    Numer = (numer1 * denom2) + (numer2 * denom1)
    Denom = denom1 * denom2
    Gcd = math.gcd(Numer,Denom)
    
    answer = [Numer // Gcd, Denom // Gcd]
    
    return answer