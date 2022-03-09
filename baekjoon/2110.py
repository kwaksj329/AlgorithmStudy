import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for i in range(n):
  house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:

  mid = (start + end) // 2

  put = 1
  prev = house[0]
  for i, h in enumerate(house):
    if i > 0:
      if h - prev >= mid:
        put += 1
        prev = h

  if put >= c:
    start = mid +1
    if result < mid:
      result = mid
  else:
    end = mid -1

print(result)
