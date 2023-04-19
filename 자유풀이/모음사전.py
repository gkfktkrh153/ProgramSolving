lst1 = []
count = 0
answer = 0

def func(n,lst): 
    global count
    global answer
    print(lst1)
    if lst1 == lst: answer = count
    if n == 5:  return
    
    for i in range(1,6):
        lst1.append(i) 
        count += 1 
        func(n+1,lst)
        del lst1[n]
        
def solution(word):
    lst = []
    for i in word:
        if i == 'A':    lst.append(1)
        elif i == 'E':  lst.append(2)
        elif i == 'I':  lst.append(3)
        elif i == 'O':  lst.append(4)
        elif i == 'U':  lst.append(5)
    
    global answer
    answer = 0
    
    func(0,lst)
    return answer