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
        
        for i in range(4):
            if row + dy[i] >= 0 and row + dy[i] < 12 and col +dx[i] >= 0 and col + dx[i] < 6:
                if m[row + dy[i]][col + dx[i]] == word and visited[row+dy[i]][col + dx[i]] == False:
                    size += 1
                    queue.append([row + dy[i], col + dx[i]])
                    visited[row + dy[i]][col + dx[i]] = True
    
    if size >= 4:
        return puyo
    else:  
        return
def a(m):
    for i in range(6):
        swap = [11,i]
        for j in range(11,-1,-1):
            if m[j][i] != '.': # 문자를 발견했는데
                if m[swap[0]][swap[1]] == '.': # 현재 저장된 좌표가 '.'을 저장하고 있다면 바꾼다.
                    temp = m[swap[0]][swap[1]]
                    m[swap[0]][swap[1]] = m[j][i]
                    m[j][i] = temp
                    swap = [swap[0] - 1,swap[1]]
                else:                           
                    swap = [swap[0] -1, swap[1]]

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

def puyopuyo(m,pList):
    for row, col in pList:
        m[row][col] = '.'

m = []
for i in range(12):
    m.append(list(input()))

result = 0
while True:
    puyoList = getPuyoList()
    if puyoList:
        puyopuyo(m,puyoList)
        a(m)
        result += 1
    else:
        break
print(result)




