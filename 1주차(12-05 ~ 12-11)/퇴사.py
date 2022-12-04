N = int(input())
max = 0
visited = [False for _ in range(N+1)]
lst = []
T = [0 for _ in range(N+1)] #걸리는 기간
P = [0 for _ in range(N+1)] #금액

for i in range(1, N+1):
    T[i], P[i] = map(int , input().split())
#print(T,P)

def combination(level, select,  current, point):
    global max

    if (select == len(lst)): 
        print(f'list: {lst}, point: {point}')
        if point > max:
            max = point
        #print()

    for i in range(level,N+1):
        if visited[i] == False and current <= i and i + T[i] <= 1 + N:
            visited[i] = True
            lst.append(i)
            combination(level + 1, select,i + T[i], point + P[i])
            visited[i] = False
            lst.pop()

for M in range(1, N+1):
    combination(1, M, 0, 0) # combinaiton(1, M) N개중에 M개를 고름
    #print(visited)
print(max)


""""
N = int(input())
max = 0
visited = [False for _ in range(N+1)]
lst = []
T = [0 for _ in range(N+1)] #걸리는 기간
P = [0 for _ in range(N+1)] #금액

for i in range(1, N+1):
    T[i], P[i] = map(int , input().split())
#print(T,P)

def combination(level, select):
    global max
    if (select == len(lst)):
        point = 0    
        current = 0
        print(lst, end=': ')
        for i in lst: # 인덱스 조합이 넘어옴
            if current <= i and i + T[i] <= 1+N: # 상담 가능
                current = i + T[i] #상담하는날 + 걸리는 기간
                point += P[i]
                print(i,end=' ')
        if point > max:
            max = point
        print()

    for i in range(level,N+1):
        if visited[i] == False:
            visited[i] = True
            lst.append(i)
            combination(level + 1, select)
            visited[i] = False
            lst.pop()
for M in range(1, N//2):
    combination(1,M) # combinaiton(1, M) N개중에 M개를 고름

print(max)
"""

