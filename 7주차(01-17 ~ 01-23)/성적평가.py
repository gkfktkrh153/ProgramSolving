import sys


N = int(sys.stdin.readline())
total = []
for i in range(1,N+1):
    total.append([i,0])

for n in range(N):
    lst = []
    exist = {}
    l = list(map(int, sys.stdin.readline().split()))
    

    for index, point in enumerate(l, start = 1):
        lst.append([index, point])
        total[index-1][1] += point

    lst = sorted(lst, key = lambda x : -x[1])


    rank = 1
    rank_ = 1

    for lstItem in lst: ##  60 60 60 50 40
        if lstItem[1] in exist:
            rank_ += 1
            lstItem.append(rank)
            exist[lstItem[1]] = True

        else:
            rank = rank_
            rank_ += 1
            lstItem.append(rank)
            exist[lstItem[1]] = True


    lst = sorted(lst, key = lambda x : x[0])

    for a in lst:
        print(a[2], end = " ")
    print()



total = sorted(total, key = lambda x : -x[1])


rank = 1
rank_ = 1
exist = {}

for lstItem in total: ##  60 60 60 50 40
    if lstItem[1] in exist:
        rank_ += 1
        lstItem.append(rank)
        exist[lstItem[1]] = True

    else:
        rank = rank_
        rank_ += 1
        lstItem.append(rank)
        exist[lstItem[1]] = True


total = sorted(total, key = lambda x : x[0])
for i in total:
    print(i[2], end = " ")

    #[위치, 점수 ,등수]


