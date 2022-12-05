from collections import deque
dx = [0,1,0,-1] # 위, 오, 아, 왼
dy = [-1,0,1,0]

def BFS(field, row, col, visited):
    queue = deque([row,col])
    visited[row][col] =  True

    while queue:
        v = queue.popleft()
        for i in range(4):
            if row + dy[i] >= 0 and row + dy[i] < 12 and col +dx[i] >= 0 and col + dx[i] < 6:
                if visited[row + dy[i]][col + dx[i]] == False:
                    queue.append([row +dy[i], col + dx[i]])
                    visited[row + dy[i]][col + dx[i]] = True

field = []
visited = [[False for j in range(6)] for i in range(12)]
for i in range(12):
    lst = list(input())
    field.append(lst)
for f in field:
    print(f)

