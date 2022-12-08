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

gear = [[1,0,1,0,1,1,1,1]]

visited = [[True,0] for i in range(4)]
for j in range(4):
    if visited[0][0] == True:
        rotation(0,-1)
        print(gear)