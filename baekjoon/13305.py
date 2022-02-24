import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

all = []
all.append([road])
a = all[:]

for j in range(n-2):

  realtemp = []

  for temp in a:
    for i in range(1, len(temp)):
      new = temp[:]
      new[i-1] += new[i]
      del new[i]
      realtemp.append(new)
      all.append(new)
      print(new, realtemp, a)    

  a = realtemp[:]
