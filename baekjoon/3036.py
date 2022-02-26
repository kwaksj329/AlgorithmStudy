import sys
import math
input = sys.stdin.readline

n = int(input())
all = list(map(int, input().split()))

main = all[0]

for a in range(1, len(all)):
  gcd = math.gcd(main, all[a])
  print(int(main/gcd), end='/')
  print(int(all[a]/gcd))
