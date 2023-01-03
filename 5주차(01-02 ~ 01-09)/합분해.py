m = [[0 for i in range(201)] for j in range(201)]
a, b = list(map(int, input().split()))

for i in range(1,201):
  m[i][0] = 1
for i in range(201):
  m[1][i] = 1

for i in range(2, 201):
  for j in range(1, 201):
    m[i][j] = m[i-1][j] + m[i][j-1]

print(m[b][a] % 1000000000)
