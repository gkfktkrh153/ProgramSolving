def solution(k, tangerine):
    lst = [[]for i in range(10000001)]
    for i in tangerine:
        lst[i].append(i)
    lst.sort(key = lambda x:len(x), reverse = True)

    answer = 0
    for l in lst:
        answer += 1
        k = k - len(l)

        if k <= 0:
            break
            
    return answer