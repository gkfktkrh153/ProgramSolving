def solution(x):
    strX = str(x)
    a = 0
    for s in strX:
        a += int(s)
    answer = False
    if x % a == 0:
        answer = True
    
    return answer