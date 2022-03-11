import sys
input = sys.stdin.readline

t = int(input())

arr = [0] * 101

arr[1] = 1
arr[2] = 1
arr[3] = 1

for i in range(t):

    n = int(input())

    if n >= 4:

        for i in range(4, 101):
            arr[i] = arr[i-2] + arr[i-3]
            if n == i:
                print(arr[n])
                break

    else:
        print(arr[n])