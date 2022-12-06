m = []


for i in range(12):
    lst = m.append(list(input()))



for i in range(6):
    swap = [11,i]
    for j in range(11,-1,-1):
        if m[j][i] != '.': # 문자를 발견했는데
            if m[swap[0]][swap[1]] == '.': # 현재 저장된 좌표가 '.'을 저장하고 있다면 바꾼다.
                temp = m[swap[0]][swap[1]]
                m[swap[0]][swap[1]] = m[j][i]
                m[j][i] = temp
                swap = [swap[0] - 1,swap[1]]
            else:
                swap = [swap[0] -1, swap[1]]

for m_ in m:
    print(m_)




