N = int(input())
dp = []
lst = []
for i in range(N):
    l = list(map(int, input().split()))
    lst.append(l)
    dp.append([0 for j in range(N)])

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        distance = lst[i][j]
        if dp[i][j] != 0 and lst[i][j] != 0:# 도착지점이 아니고 해당 위치에 도달하는 루트가 존재할 경우
            if i + distance < N:   # 현재 위치에서 이동 가능한 경우
                dp[i + distance][j] += dp[i][j] # 현재 위치까지 도달할 수 있는 모든 루트의 수를 더해준다. 
            if j + distance < N:
                dp[i][j + distance] += dp[i][j]

print(dp[N-1][N-1])
