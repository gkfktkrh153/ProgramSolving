import sys

input = sys.stdin.readline
lst = []

str = input()
dp = [0 for _ in range(len(str))]
n = int(input())
for i in range(n): lst.append(input().rstrip())

for i in range(len(str)): # softwarecontest
    if dp[i] or i == 0:
        lgth = i


        for j in lst: # software, contest, softwarecontests 
            if lgth + len(j) > len(str): continue
            flag = 1
            for k in range(len(j)):
                if j[k] != str[lgth+k]:
                    flag = 0; break
            if flag:
                dp[lgth+len(j)] = 1 # dp[8] = 1 dp[15] = 1
                # str - softwarecontest
                # software
                # contest

print(dp[len(str)-1])