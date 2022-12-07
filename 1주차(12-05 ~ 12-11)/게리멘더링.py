from itertools import combinations

def segmentation(lst):
    one, two = -1, -1
    for i in range(1,N+1):
            if i in l: # 1구역
                area[i] = 1
                one = i
            else: #2구역
                area[i] = 2
                two = i
    return one, two
     
def DFS(start,areaNum):
    visited[start] = True

    for next in graph[start]: # start와 연결된 지점
        if visited[next] == False and area[next] == areaNum: # 아직 방문하지 않았고, 탐색중인 지역구 일 때
            DFS(next, areaNum)
    


N = int(input())

population = list(map(int, input().split()))
population.insert(0, 0)
area = [0 for i in range(N+1)]
visited = [False for i in range(N+1)]



graph = [[] for i in range(N+1)]
for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    graph[i] = lst[1:]
#print(graph)

min = 100000000
possible = False
for i in range(1,N+1):
    lst = list(combinations([num for num in range(1, N+1)],i)) # N C R
    for l in lst: # [[1,2],[1,3],[1,4],[1,5]]
        one, two = segmentation(l) # 구역할당 + 1구역원소, 2구역원소 하나씩 리턴
        visited = [False for i in range(N+1)]
        
        DFS(one, 1) # 1구역 DFS
        DFS(two, 2) # 2구역 DFS
        if visited.count(True) < N: #불가능한 방법
            continue
        #가능한 방법
        possible = True

        firstArea = 0  # 1구역 인구합
        secondArea = 0 # 2구역 인구합
        for index in range(1,N+1):
            if area[index] == 1:
                firstArea += population[index]
            else:
                secondArea += population[index]
        if min > abs(firstArea - secondArea):
            min = abs(firstArea - secondArea)
        
if possible == False:
    print(-1)
else:
    print(min)
        


