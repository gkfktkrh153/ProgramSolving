N = int(input())
crane = list(map(int, input().split()))
M = int(input())

box = list(map(int, input().split()))
box.sort()

result = 0
for i in range(M):
    if crane[i % N] < box[i]: # 크레인이 박스를 못실을 때
        result = -1
    if i % N == 0:
        result += 1
print(result)
