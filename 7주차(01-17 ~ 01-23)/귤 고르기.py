def solution(k, tangerine):
    # [1,2,2,3,3,4,5,5]
    dic = {}
    for item in tangerine:
        if item in dic:
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
    lst = sorted(dic.items(), key = lambda x : -x[1])
    
    answer = 0
    for num in lst:
        k -= num[1]
        answer += 1
        
        if k <= 0:
            break
        
    
    return answer