import sys
n = int(sys.stdin.readline())

lst = []
for i in range(n):
  lst.append(int(sys.stdin.readline()))



endIndex = len(lst) - 1

result = 0
for i in range(endIndex - 1, -1 , -1):
  #print(lst)
  if lst[i] >= lst[i + 1]:
    diff = lst[i] - lst[i+1]
    result += diff + 1
    lst[i] = lst[i] - (diff + 1)
  
print(result)