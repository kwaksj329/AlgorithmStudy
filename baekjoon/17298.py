import sys
input = sys.stdin.readline

n = int(input())

number = list(map(int, input().split()))
ans = [-1]
maximum = number.pop()

while number:
  
  temp = number.pop()

  if number:
    if temp > number[-1]:
      ans.append(temp)
      maximum = temp
    else:
      if number[-1] >= temp:
        ans.append(-1)
      else:
        ans.append(maximum)


for j in range(1, len(ans)+1):
  
  if j < len(ans):
    print(ans[-j], end=' ')
  else:
    print(ans[-j])
