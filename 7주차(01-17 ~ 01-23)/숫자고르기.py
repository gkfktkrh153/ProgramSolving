import sys
result = {}
result = set(result)
def DFS(current, depth,stack):
  global result
  for next in graph[current]:
    if visited[next] == True: # 사이클
      result = result | set(stack)
    if visited[next] == False:
      visited[next] = True
      DFS(next, depth + 1, stack + [next])  
      visited[next] = False

n = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n+1)]


for i in range(1,n+1):
  node = int(sys.stdin.readline())
  graph[node].append(i)
  
#print(graph)

for i in range(1,n+1):
  if visited[i] == False:
    DFS(i,0, [])

result = sorted(result)
print(len(result))
for i in result:
  print(i)
  