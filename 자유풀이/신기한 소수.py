import sys, math

def is_prime(number):
    number = int(number)
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

def dfs(num):
  if len(num) == N:
    print(num)
  
  for tailNumber in tailNumbers:
    next = num + tailNumber
    if is_prime(int(next)):
      dfs(next)
  return 1


headNumbers = ['2','3','5','7']
tailNumbers = ['1','3','7','9']

N = int(sys.stdin.readline())


for headNumber in headNumbers:
  print(dfs(headNumber))


