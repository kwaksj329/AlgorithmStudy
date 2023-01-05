import sys
input = sys.stdin.readline

n = int(input())
video = []

for i in range(n):
  video.append(str(input())[:-1])

ans = ""

def compress(video):

  global ans
  start = video[0][0]
  same = True
  for v in video:
    for i in v:
      if i != start:
        same = False
        break

  if same:
    temp = str(start)
    ans += temp

  else:
    ans += "("
    first = []
    second = []
    third = []
    fourth = []
    for i, v in enumerate(video):
      if i < len(v)//2:
        first.append(v[:len(v)//2])
        second.append(v[len(v)//2:])
      else:
        third.append(v[:len(v)//2])
        fourth.append(v[len(v)//2:])

    compress(first)
    compress(second)
    compress(third)
    compress(fourth)

    ans += ")"

compress(video)

print(ans)
