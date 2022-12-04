from itertools import combinations

dx = [0,1,0,-1] # 위, 오, 아, 왼
dy = [-1,0,1,0]
def DFS(x, y):
    global wall
    m[y][x] = 1
    wall += 1
    #print(y, x)
    for i in range(4):
        if y + dy[i] >= 0 and y + dy[i] < N and x +dx[i] >= 0 and x + dx[i] < M:
            if m[y + dy[i]][x + dx[i]] == 0 or m[y + dy[i]][x + dx[i]] == 2:
                DFS(x + dx[i], y + dy[i])



N, M = map(int, input().split()) # N은 세로 M은 가로
#visited = [[False for j in range(M)] for _ in range(N)]

m1 = []
for row in range(N):
    lst = list(map(int,input().split()))
    m1.append(lst)
max = 0
l = []
w = 0
for row in range(N):
    for col in range(M):
        if m1[row][col] == 1:
            w += 1
        elif m1[row][col] == 0:
            l.append(row * M + col)

#print(l)
combi = list(combinations(l, 3))

for c in combi:
    m = []
    for k in range(N):
        m.append(m1[k].copy())
    wall = w
    for num in c:
        m[num // M][num % M] = 1


    for row in range(N):
        for col in range(M):
            if m[row][col] == 2:
                DFS(col,row)
    if N*M - (wall+3) > max:
        #print(N*M - (wall+3), m)
        max = N * M - (wall+3)
print(max)