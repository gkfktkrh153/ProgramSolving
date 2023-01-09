T = int(input())
lst = []
for i in range(T):
  l = list(map(str, input()))
  lst.append(l)
print(lst)



used = {'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,'G':False,'H':False,'I':False,'J':False
,'K':False,'L':False,'M':False,'N':False,'O':False,'P':False,'Q':False,'R':False,'S':False,'T':False,'U':False }

number = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0
,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0 }



n = 9
while(lst):
  lst.sort(reverse=True)  
  c = lst[0][0]
  
  if used[c] == False: # 가장 큰 자리수에 위치한 알파벳을 사용하지 않았다면
    number[c] = n
  lst[0].pop(0)

print(number)


    


