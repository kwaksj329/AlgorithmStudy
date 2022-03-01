import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):

    n = int(input())
    zero = [1, 0]
    one = [0, 1]

    if n == 0:
        now = zero
    elif n == 1:
        now = one

    for i in range(n-1):
        now = [zero[0]+one[0], zero[1]+ one[1]]
        zero = one
        one = now

    print(*now)
    