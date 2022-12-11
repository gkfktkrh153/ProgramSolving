def solution(s):
    dic = {}
    answer = []
    for c in range(97,123):
        dic[chr(c)] = -1
    for i, w in enumerate(s):
        if dic[w] == -1:
            answer.append(-1)
        else:
            answer.append(i - dic[w])        
        
        dic[w] = i 
            
    #print(dic)

    return answer