import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
number = list(map(int, input().split()))

for num in number:

  start = 0
  end = n-1
  find = False
  while start <= end:

    mid = (end + start)//2

    if num == a[mid]:
      find = True
      print(1)
      break
    elif num < a[mid]:
      end = mid-1
    elif num > a[mid]:
      start = mid+1

  if not find:
    print(0)
