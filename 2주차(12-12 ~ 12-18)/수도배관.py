import sys

D, P = map(int, sys.stdin.readline().split())
LC = [list(map(int, sys.stdin.readline().split())) for _ in range(P)]
DP = [0 for _ in range(D+1)]
for i in range(P):
    for j in range(D+1):
        if j >= LC[i][0] and DP[j] != 0:
            DP[j-LC[i][0]] = max(DP[j-LC[i][0]], min(LC[i][1], DP[j]))
    if LC[i][1] > DP[D-LC[i][0]]:
        DP[D-LC[i][0]] = LC[i][1]

print(DP[0])