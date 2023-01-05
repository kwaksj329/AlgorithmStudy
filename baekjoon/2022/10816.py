import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))

number.sort()
cnumber = Counter(number)
dict(sorted(cnumber.items()))

ans = ''

for c in card:
  if c in cnumber:
    ans += str(cnumber[c])
    ans += ' '

  else:
    ans += '0 '
print(ans[:-1])
