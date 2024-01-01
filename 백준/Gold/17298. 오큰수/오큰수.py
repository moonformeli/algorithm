import sys

N = int(sys.stdin.readline())
stack_a = list(map(int, input().split()))
stack_b = []

res = [-1] * N
i = N - 1

while i >= 0:
    num = stack_a.pop()

    while len(stack_b) > 0:
        if num < stack_b[-1]:
            res[i] = stack_b[-1]
            stack_b.append(num)
            break
        else:
            stack_b.pop()

    if len(stack_b) == 0:
        stack_b.append(num)

    i -= 1


print(*res, sep=" ")
