import sys
input = sys.stdin.readline

n = str(input())[:-1]
all = []

for i in range(len(n)):
  all.append(int(n[i]))

all.sort(reverse = True)
temp = ''
for i in all:
  temp += str(i)

temp = int(temp)
print(temp)
