from collections import deque

dx = [0,1,0,-1] # 위, 오, 아, 왼
dy = [-1,0,1,0]
size = 0

def BFS(m, row, col, visited,word):
    global size
    queue = deque([[row, col]])
    visited[row][col] = True
    size += 1
    puyo = []
    while queue:
        row, col = queue.popleft()
        puyo.append([row, col])
        print(word, row, col, size)
        
        for i in range(4):
            if row + dy[i] >= 0 and row + dy[i] < 12 and col +dx[i] >= 0 and col + dx[i] < 6:
                if m[row + dy[i]][col + dx[i]] == word and visited[row+dy[i]][col + dx[i]] == False:
                    size += 1
                    queue.append([row + dy[i], col + dx[i]])
                    visited[row + dy[i]][col + dx[i]] = True
    print(word, size)
    if size >= 4:
        return puyo
    else:  
        return


def printMap(map):
    for m_ in map:
        print(m_)
    print()

def getPuyoList():
    visited = [[False for i in range(6)] for j in range(12)]
    pList = []
    global size
    for i in range(12):
        for j in range(6):
            if m[i][j] != '.' and visited[i][j] == False:
                size = 0
                result = BFS(m, i ,j ,visited, m[i][j])
                if result:
                    pList = pList + result
    return pList

def puyopuyo(pList):
    for row, col in pList:
        m[row][col] = '.'

m = []
for i in range(12):
    m.append(list(input()))

result = 0
while True:
    puyoList = getPuyoList()
    if puyoList:
        print(puyoList)
        puyopuyo(puyoList)
        printMap(m)
        result += 1
    else:
        break
print(result)




