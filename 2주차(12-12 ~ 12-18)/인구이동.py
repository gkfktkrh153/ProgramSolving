from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def reLocation(l):

  for loc in l:
    sum = 0
    for row, col in loc:
      sum += m[row][col]
    for row, col in loc:
      m[row][col] = sum // len(loc)

def BFS(row, col):
  global count
  global sum
  queue = deque([(row, col)])
  visited[row][col] = True
  location.append((row,col))

  while queue:
    row, col = queue.popleft()
    for i in range(4):
      y = row + dy[i]
      x = col + dx[i]
      if 0 <= y < N and 0 <= x < N:
        if visited[y][x] == False and L <= abs(m[row][col] - m[y][x]) <= R:
          queue.append((y,x))
          visited[y][x] = True
          location.append((y,x))
  #print("location" , location)
  if len(location) > 1: # 연합
    return location
    
  



N, L, R = map(int, input().split())


m = []
for i in range(N):
  m.append(list(map(int, input().split())))
visited = [[False for i in range(N)] for j in range(N)]
count = 0
result = 0
location = []

while(True):
  count = 0
  sum = 0

  l = []
  visited = [[False for i in range(N)] for j in range(N)]
  for row in range(N):
    for col in range(N): 
      if visited[row][col] == False:
        location =[]
        lo = BFS(row,col) 
        if lo != None:
          l.append(lo) 

  if l == []:
    break     
  #print("l", l)
  reLocation(l)

  result += 1
  #print(m)

print(result)
