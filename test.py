from itertools import combinations

nums = [1,2,3,4]
perm = list(combinations(nums, 2))
print(perm)

lst = [[1,2,3,4],[5,6,7,8]]
for i in range(10):
    print(i, end= ' ')
    print(i // 5, end= ' ')
    print(i % 5, end= ' ')
    print()