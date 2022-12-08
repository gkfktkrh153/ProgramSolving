def rotation(num, direction):
    temp = gear[num][0]
    if direction == 1:
        for i in range(7, 0, -1): # 0 ~ 7
            gear[num][(i + 1) % 8] = gear[num][i % 8]
        gear[num][1] = temp
    else:
        for i in range(0,8):
             gear[num][i] = gear[num][(i + 1) % 8]
        gear[num][7] = temp

def dfs(current, direction):
    visited[current][0] = True
    visited[current][1] = direction
    
    if direction == 1:
        d = -1
    else:
        d = 1
    for i in range(2):
        next = current + dx[i]
        if 0 <= next and next < 4 and visited[next][0] == False: # 범위 내
            if i == 0: # 오른쪽
                if gear[current][2] != gear[next][6]: #
                    dfs(next, d)  
            else: #왼쪽
                if gear[current][6] != gear[next][2]:
                    dfs(next, d)

dx = [1,-1]

gear = []
for i in range(4):
    gear.append(list(map(int, input())))

visited = [[False,0] for i in range(4)]
k = int(input())# 회전횟수
for i in range(k):
    num, direction = map(int, input().split())
    num = num-1
    visited = [[False,0] for a in range(4)]
    dfs(num, direction)

    for index in range(4):
        if visited[index][0] == True:
            rotation(index, visited[index][1])
sum = 0
for i in range(4):
    if gear[i][0] == 1:
        sum += 2 ** i
print(sum)
