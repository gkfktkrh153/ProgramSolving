time = 0
def serch(current):
  global time
    
  visited[current] = True
  print(f'{name[current]}에 도착했습니다.')

  select = []
  for i in range(len(graph[current])):
    if visited[i] == False and graph[current][i]: 
      select.append(i)
      
  if select == []:
    return

  print('이동할 곳을 선택하십시오.(', end='')  
  for i in range(len(select)):
    print(f'{i + 1}. {name[select[i]]}',end=' ')


  s = int(input(') ==>  ')) - 1  
  next = select[s]
  time += graph[current][next]
  print('소모시간',graph[current][next])
  serch(next)

name = ["출발", "기흥역", "학교앞", "강의실", "편의점", "식당", "교학팀", "서울역", "숙대입구역", "헬스장", "집"]
출발, 기흥역, 학교앞, 강의실, 편의점, 식당, 교학팀, 서울역, 숙대입구역, 헬스장, 집 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
visited = [False for i in range(11)]
graph = [[0 for j in range(11)] for i in range(11)]

graph[출발][기흥역] = 60
graph[출발][학교앞] = 70
graph[학교앞][강의실] = 20
graph[기흥역][학교앞] = 15
graph[기흥역][강의실] = 30
graph[강의실][식당] = 20
graph[강의실][편의점] = 10
graph[식당][교학팀] = 10
graph[편의점][교학팀] = 5
graph[교학팀][서울역] = 70
graph[교학팀][숙대입구역] = 80
graph[서울역][헬스장] = 20
graph[서울역][집] = 10
graph[서울역][숙대입구역] = 20
graph[숙대입구역][헬스장] = 5
graph[헬스장][집] = 10  

serch(출발)
print(f'총 이동시간: {time// 60}시간 {time%60}분')
