from collections import deque


dy = [-1,0,1,0]
dx = [0,1,0,-1]

def BFS(row, col):
  visited[row][col] = True
  queue = deque([(row, col)])
  
  while(queue):
    row, col = queue.popleft()

    for i in range(4):
      y = row + dy[i]
      x = col + dx[i]
      if 0 <= y < N and 0 <= x < N: # 범위 내
        if visited[y][x] == False:
          queue.append((y,x))
          visited[y][x] = True


N = int(input())

m = []

for i in range(N):
  lst = list(map(int, input().split()))
  m.append(lst)



max = 0
for i in range(0,101):
  visited = [[False for col in range(N)] for row in range(N)] # 물에 잠기는 곳 여부
  for j in range(N): # 물에 잠김 체크
    for k in range(N):
      if m[j][k] <= i:
        visited[j][k] = True
  
  count = 0
  for j in range(N):
    for k in range(N):
      if visited[j][k] == False: # 잠기지 않은 영역 탐색
        BFS(j,k)
        count += 1
  if max < count:
    max = count
print(max)


