def swap(i1, i2):
  global str
  temp = str[i1]
  str[i1] = str[i2]
  str[i2] = temp

N1, N2 = list(map(int, input().split()))

a = list(input())
b = list(input())

T = int(input())

a.reverse()
str = a + b

for t in range(T):
  index = []
  for k in range(len(str) - 1):
    if (str[k] in a and str[k+1] in b):
      index.append(k)
  for i in index:
    swap(i, i + 1)
  

print(''.join(str))


"""
A - 1234  B - 567

1235467

1253647

1526374

5162734

5617234


"""
