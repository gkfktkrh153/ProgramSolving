class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
stack = []
visitedAry = ['집', '신림역', '강남역', '서울역', '강남대역', '학교']
집, 신림역, 강남역, 서울역, 강남대역, 학교 = 0, 1, 2, 3, 4, 5

G1 = Graph(6)
G1.graph[집][신림역] = 20; G1.graph[집][서울역] = 50
G1.graph[신림역][집] = 20; G1.graph[신림역][강남역] = 20
G1.graph[강남역][신림역] = 20; G1.graph[강남역][강남대역] = 50
G1.graph[서울역][집] = 50; G1.graph[서울역][강남대역] = 60
G1.graph[강남대역][강남역] = 50; G1.graph[강남대역][서울역] = 60; G1.graph[강남대역][학교] = 10
G1.graph[학교][강남대역] = 10

print('집에서 학교 가는 전체 연결도')
print(' ', end= ' ')
for v in range(G1.SIZE):
    print(visitedAry[v], end = ' ')
print()
for row in range(G1.SIZE):
    print(visitedAry[row], end = ' ')
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end = ' ')
    print()
print()

#current = 0
#stack.append(current)
#visitedAry.append(current)

print(visitedAry)
while (len(stack) !=0):
    next = None
    for vertex in range(6):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문 순서 -->', end = ' ')

for i in visitedAry:
    print(i, end= ' ')

    #print(str(ord('집')+i), end = ' ')