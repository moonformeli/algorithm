import sys

n = int(sys.stdin.readline())
first_inputs = set(map(int, input().split()))
m = int(sys.stdin.readline())
second_inputs = map(int, input().split())

for i in second_inputs:
    if i in first_inputs:
        print(1)
    else:
        print(0)
