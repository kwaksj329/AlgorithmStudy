import sys
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))
allTF = True
allday = sum(data)
if allday==0:
  allTF = False

start = sum(data[:x])
maxnum = start
days = 1

for i in range(x, n):

  start += data[i]
  start -= data[i-x]

  if start > maxnum:
    maxnum = start
    days = 1
  elif start == maxnum:
    days += 1

if allTF:
  print(maxnum)
  print(days)
else:
  print("SAD")
