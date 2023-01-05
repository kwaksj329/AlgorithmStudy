import sys
import copy
input = sys.stdin.readline

first = str(input())[:-1]
second = str(input())[:-1]

start = 0
index = 0
ans = 0

while start < len(first)-1:

    index = start
    tempans = 0
    next = 0

    for f in first[index:]:

        if next > len(second)-1:
            break

        if f == second[next]:
            next += 1
            tempans += 1
            continue
        
        temp = second[next:].find(f)
        if temp != -1:
            next = temp + 1
            tempans += 1
            if temp == len(second)-1:
                break

    start += 1
    if tempans > ans:
        ans = tempans

firstans = ans

start = 0
index = 0
ans = 0

while start < len(second)-1:

    index = start
    tempans = 0
    next = 0

    for f in second[index:]:

        if next > len(first)-1:
            break
        
        temp = first[next:].find(f)
        if temp != -1:
            next = temp + 1
            tempans += 1
            print(f, temp, next, first[8])
            if temp == len(first)-1:
                break

    start += 1
    if tempans > ans:
        ans = tempans

secondans = ans
print(firstans, secondans)
if secondans > firstans:
    print(secondans)
else:
    print(firstans)