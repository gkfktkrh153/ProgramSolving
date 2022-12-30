N = int(input())
p = list(map(int, input().split()))
p.insert(0,0)

dp = [0 for i in range(len(p))]

dp[1] = p[1]

for i in range(2,len(p)): # 3
  for j in range(1,i + 1): # 1 ~ 3
    dp[i] = max(dp[i], dp[i - j] + p[j])
print(dp[N])